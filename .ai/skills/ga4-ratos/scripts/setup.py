#!/usr/bin/env python3
"""
GA4 Ratos - Setup OAuth

Uso:
  python setup.py oauth
"""

import hashlib
import os
import re
import socket
import sys
import webbrowser
from urllib.parse import unquote

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(SCRIPT_DIR)
SKILLS_DIR = os.path.dirname(SKILL_DIR)
ENV_PATH = os.path.join(SKILLS_DIR, ".env")
LEGACY_ENV_PATH = os.path.join(SKILL_DIR, ".env")
GOOGLE_ADS_ENV_PATH = os.path.join(os.getcwd(), ".ai", "skills", ".env")
LEGACY_GOOGLE_ADS_ENV_PATH = os.path.join(os.getcwd(), ".ai", "skills", "google-ads-ratos", ".env")
SCOPE = "https://www.googleapis.com/auth/analytics.readonly"
SERVER = "127.0.0.1"
OAUTH_PORT = 8080


def parse_env(path):
    if not os.path.isfile(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            value = value.strip().strip('"').strip("'")
            if key and value and not os.environ.get(key):
                os.environ[key.strip()] = value


def mask_token(token):
    if not token or len(token) < 10:
        return "***"
    return f"{token[:6]}...{token[-4:]}"


def is_port_free(port=OAUTH_PORT):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((SERVER, port))
        s.close()
        return True
    except OSError:
        return False


def get_oauth_client():
    parse_env(ENV_PATH)
    parse_env(LEGACY_ENV_PATH)
    parse_env(GOOGLE_ADS_ENV_PATH)
    parse_env(LEGACY_GOOGLE_ADS_ENV_PATH)

    client_id = os.environ.get("GA4_CLIENT_ID") or os.environ.get("GOOGLE_ADS_CLIENT_ID")
    client_secret = os.environ.get("GA4_CLIENT_SECRET") or os.environ.get("GOOGLE_ADS_CLIENT_SECRET")
    if not client_id or not client_secret:
        print("ERRO: Defina GA4_CLIENT_ID/GA4_CLIENT_SECRET ou configure google-ads-ratos.", file=sys.stderr)
        sys.exit(1)
    return client_id, client_secret


def run_oauth():
    try:
        from google_auth_oauthlib.flow import Flow
    except ImportError:
        print("ERRO: google-auth-oauthlib nao instalado.", file=sys.stderr)
        print("  Instale com: pip install google-auth-oauthlib", file=sys.stderr)
        sys.exit(1)

    client_id, client_secret = get_oauth_client()
    port = OAUTH_PORT
    if not is_port_free(port):
        print(f"ERRO: Porta {port} ocupada. Fecha o processo usando {SERVER}:{port} e tenta de novo.", file=sys.stderr)
        sys.exit(1)

    redirect_uri = f"http://{SERVER}:{port}"
    client_config = {
        "installed": {
            "client_id": client_id,
            "client_secret": client_secret,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
        }
    }

    flow = Flow.from_client_config(client_config, scopes=[SCOPE])
    flow.redirect_uri = redirect_uri

    state = hashlib.sha256(os.urandom(1024)).hexdigest()
    authorization_url, _ = flow.authorization_url(
        access_type="offline",
        state=state,
        prompt="consent",
        include_granted_scopes="false",
    )

    print()
    print("=" * 60)
    print("  AUTORIZACAO GA4")
    print("=" * 60)
    print()
    print("Abre esta URL no browser (ou ela vai abrir sozinha):")
    print()
    print(f"  {authorization_url}")
    print()
    print(f"Aguardando callback em {redirect_uri} ...")
    print()

    webbrowser.open(authorization_url)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((SERVER, port))
    sock.listen(1)

    try:
        connection, _ = sock.accept()
        data = connection.recv(4096).decode("utf-8")
    except KeyboardInterrupt:
        print("\nCancelado pelo usuario.")
        sock.close()
        sys.exit(1)

    match = re.search(r"GET\s\/\?(.*?)\s", data)
    if not match:
        connection.close()
        sock.close()
        print("ERRO: Callback invalido recebido do Google.", file=sys.stderr)
        sys.exit(1)

    params = {}
    for pair in match.group(1).split("&"):
        if "=" in pair:
            k, v = pair.split("=", 1)
            params[k] = unquote(v)

    html = (
        "<html><head><meta charset='utf-8'></head><body style='font-family:sans-serif;"
        "display:flex;align-items:center;justify-content:center;height:100vh;'>"
        "<div style='text-align:center;'><h1>Pronto</h1>"
        "<p>GA4 autorizado com sucesso. Pode fechar esta aba.</p></div></body></html>"
    )
    response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html}"
    connection.sendall(response.encode())
    connection.close()
    sock.close()

    if "error" in params:
        print(f"ERRO do Google: {params['error']}", file=sys.stderr)
        sys.exit(1)

    code = params.get("code", "")
    if not code:
        print("ERRO: Nenhum authorization code recebido.", file=sys.stderr)
        sys.exit(1)

    flow.fetch_token(code=code)
    refresh_token = flow.credentials.refresh_token
    if not refresh_token:
        print("ERRO: Google nao retornou refresh token. Revogue o app e tente novamente.", file=sys.stderr)
        sys.exit(1)

    save_ga4_oauth(client_id, client_secret, refresh_token)
    print(f"Refresh token GA4 gerado: {mask_token(refresh_token)}")
    print(f"Salvo em {ENV_PATH}")


def upsert_env(content, key, value):
    line = f'{key}="{value}"'
    if re.search(rf"^{re.escape(key)}=.*$", content, flags=re.MULTILINE):
        return re.sub(rf"^{re.escape(key)}=.*$", line, content, flags=re.MULTILINE)
    return content.rstrip("\n") + "\n" + line + "\n"


def save_ga4_oauth(client_id, client_secret, refresh_token):
    if not os.path.isfile(ENV_PATH):
        print(f"ERRO: .env nao encontrado em {ENV_PATH}", file=sys.stderr)
        sys.exit(1)
    with open(ENV_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    content = upsert_env(content, "GA4_CLIENT_ID", client_id)
    content = upsert_env(content, "GA4_CLIENT_SECRET", client_secret)
    content = upsert_env(content, "GA4_REFRESH_TOKEN", refresh_token)
    with open(ENV_PATH, "w", encoding="utf-8") as f:
        f.write(content)


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "oauth":
        print("Uso: python setup.py oauth")
        sys.exit(1)
    run_oauth()
