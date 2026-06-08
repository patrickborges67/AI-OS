"""Monta carousel.html (export full-size) + preview.html (revisao navegavel).
Layout: imagem no topo + faixa preta dedicada embaixo para o texto (como o
criativo vencedor). O UGC (c6) e excecao: texto sobre a imagem com gradiente.
Estilo: design-guide da Lumina (Cormorant Garamond, dourado, estrela 8 pontas).
"""
import base64
from pathlib import Path

BASE = Path(__file__).resolve().parent
SRC = BASE.parent / "novos-criativos"

def b64(name):
    return "data:image/png;base64," + base64.b64encode((SRC / name).read_bytes()).decode("ascii")

PRICE = """
          <div class="price-row">
            <span class="price-big">R$2,49</span>
            <span class="price-unit">POR FOTO</span>
          </div>
          <div class="price-sub">Pacote completo &middot; 10 fotos por R$24,90</div>"""

SLIDES = [
    {"img": "c1-resultado-base.png", "kicker": "ESTÚDIO LUMINA",
     "title": "DO CELULAR AO ENSAIO", "price": True, "oneline": True},
    {"img": "c2-sem-pose.png", "kicker": "ENSAIO DE ANIVERSÁRIO COM IA",
     "title": "SEM POSE. SEM VERGONHA.", "price": True},
    {"img": "c3-prova.png", "kicker": "RESULTADO REAL",
     "title": "O ENSAIO QUE ELA NÃO ESPERAVA", "price": True},
    {"img": "c4-dualidade.png", "kicker": "COMPARE",
     "title": "TRADICIONAL: R$300+ &nbsp; <span class='vs'>COM IA: R$24,90</span>",
     "price": False, "title_small": True, "tight": True},
    {"img": "c5.png", "kicker": "SEU ANIVERSÁRIO MERECE",
     "title": "VOCÊ, NA SUA MELHOR VERSÃO", "price": True},
    {"img": "c6.png", "ugc": True,
     "title": "Seu aniversário tá chegando<br>e você <em>ainda não tem</em><br>nenhuma foto boa?",
     "cta": "CHAMA NO WHATSAPP →"},
]

def slide_inner(s):
    if s.get("ugc"):
        return f"""      <div class="photo full" style="background-image:url('{b64(s['img'])}');">
        <div class="ugc-overlay">
          <p class="ugc-title">{s['title']}</p>
          <div class="cta">{s['cta']}</div>
        </div>
      </div>"""
    title_cls = "title small" if s.get("title_small") else "title"
    if s.get("oneline"):
        title_cls += " oneline"
    bar_cls = "bar tight" if s.get("tight") else "bar"
    kicker = f"""<div class="kicker"><span class="star">&#10022;</span> {s['kicker']} <span class="star">&#10022;</span></div>""" if s.get("kicker") else ""
    right = f'<div class="bar-right">{PRICE}</div>' if s.get("price") else ""
    return f"""      <div class="photo" style="background-image:url('{b64(s['img'])}');"></div>
      <div class="{bar_cls}">
        <div class="bar-left">
          {kicker}
          <h1 class="{title_cls}">{s['title']}</h1>
        </div>
        {right}
      </div>"""

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;0,800;1,600&display=swap');
* { margin:0; padding:0; box-sizing:border-box; }
.slide {
  width:1080px; height:1080px; position:relative; background:#0A0A0A;
  overflow:hidden; font-family:'Playfair Display', Georgia, serif;
}
/* imagem preenche o quadrado inteiro (sem corte de faixa); texto sobreposto na base */
.photo { position:absolute; inset:0; background-size:cover; background-position:center; }
.bar {
  position:absolute; left:0; right:0; bottom:0; color:#F5F0E8;
  padding:24px 58px 36px;
  display:flex; flex-direction:row; align-items:flex-end; gap:42px;
  background:linear-gradient(to bottom, transparent 0%, rgba(0,0,0,.78) 42%, rgba(0,0,0,.95) 100%);
}
.bar.tight { padding:20px 58px 32px; }
.bar-left { flex:1 1 auto; min-width:0; }
.bar-right { flex:0 0 auto; text-align:right; border-left:1px solid rgba(201,160,80,.28); padding-left:40px; }
.kicker { color:#C9A050; letter-spacing:.24em; text-transform:uppercase; font-size:18px; font-weight:600; margin-bottom:9px; }
.kicker .star { font-size:13px; }
.title { font-weight:700; color:#F5F0E8; font-size:47px; line-height:1.04; letter-spacing:.01em; }
.title.small { font-size:40px; }
.title.oneline { white-space:nowrap; font-size:38px; letter-spacing:0; }
.title .vs { color:#C9A050; }
.price-row { display:flex; align-items:baseline; gap:11px; justify-content:flex-end; }
.price-big { font-weight:800; font-size:58px; line-height:1; white-space:nowrap;
  background:linear-gradient(135deg,#E2B96A,#C9A050,#8B6520);
  -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; }
.price-unit { letter-spacing:.16em; text-transform:uppercase; color:#F5F0E8; font-size:21px; font-weight:600; white-space:nowrap; }
.price-sub { color:#D8CFBE; font-size:19px; margin-top:5px; white-space:nowrap; }
/* UGC: imagem inteira + texto no topo sobre gradiente */
.ugc-overlay { position:absolute; inset:0; padding:54px 56px; z-index:1;
  display:flex; flex-direction:column; justify-content:flex-start;
  background:linear-gradient(to bottom, rgba(0,0,0,.78) 0%, rgba(0,0,0,.4) 34%, transparent 56%); }
.ugc-title { color:#fff; font-weight:600; font-size:50px; line-height:1.14; text-shadow:0 2px 16px rgba(0,0,0,.7); }
.ugc-title em { color:#E2B96A; font-style:italic; }
.cta { display:inline-block; align-self:flex-start; margin-top:22px;
  text-transform:uppercase; letter-spacing:.14em; font-weight:700; font-size:24px; color:#0A0A0A;
  background:linear-gradient(135deg,#E2B96A,#C9A050,#8B6520); padding:12px 26px; border-radius:3px; }
"""

slides_html = "\n".join(f'    <div class="slide" id="s{i+1}">\n{slide_inner(s)}\n    </div>' for i, s in enumerate(SLIDES))

# ---- carousel.html (export full-size, slides empilhados) ----
(BASE / "carousel.html").write_text(
    f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Lumina - export</title><style>{CSS}
body{{background:#222;}}</style></head><body>
{slides_html}
</body></html>""", encoding="utf-8")

# ---- preview.html (revisao navegavel: grade escala reduzida) ----
PREVIEW_CSS = CSS + """
body { background:#15130f; margin:0; padding:40px; font-family:'Cormorant Garamond',serif; }
.pv-head { color:#C9A050; text-align:center; letter-spacing:.2em; text-transform:uppercase; margin-bottom:32px; font-size:20px; }
.grid { display:flex; flex-wrap:wrap; gap:36px; justify-content:center; }
.cell { display:flex; flex-direction:column; align-items:center; gap:10px; }
.cell .label { color:#8B6520; font-size:18px; letter-spacing:.15em; text-transform:uppercase; }
/* escala cada slide 1080 -> 380 */
.scale { width:380px; height:380px; overflow:hidden; border:1px solid rgba(201,160,80,.25); border-radius:4px; }
.scale .slide { transform:scale(0.35185); transform-origin:top left; }
"""
cells = "\n".join(
    f'      <div class="cell"><div class="scale"><div class="slide">{slide_inner(s)}</div></div>'
    f'<div class="label">Criativo {i+1}</div></div>'
    for i, s in enumerate(SLIDES)
)
(BASE / "preview.html").write_text(
    f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<title>Lumina - preview dos anuncios</title><style>{PREVIEW_CSS}</style></head><body>
  <div class="pv-head">&#10022; Est&uacute;dio Lumina &mdash; pr&eacute;via dos 6 an&uacute;ncios &#10022;</div>
  <div class="grid">
{cells}
  </div>
</body></html>""", encoding="utf-8")

print("carousel.html + preview.html gerados (6 slides, faixa dedicada).")
