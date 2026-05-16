#!/usr/bin/env python3
"""Generate or edit images with the OpenAI Images API."""

from __future__ import annotations

import argparse
import base64
import os
import sys
import urllib.request
from pathlib import Path


SIZE_ALIASES = {
    "square": "1024x1024",
    "landscape": "1536x1024",
    "portrait": "1024x1536",
}


def load_dotenv_if_available() -> None:
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError:
        return

    load_dotenv(override=False)
    shared_env = Path(__file__).resolve().parents[2] / ".env"
    if shared_env.exists():
        load_dotenv(shared_env, override=False)
    skill_env = Path(__file__).resolve().parents[1] / ".env"
    if skill_env.exists():
        load_dotenv(skill_env, override=False)
    home_env = Path.home() / ".env"
    if home_env.exists():
        load_dotenv(home_env, override=False)


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate or edit images with GPT Image 2.")
    p.add_argument("-p", "--prompt", required=True, help="Prompt or edit instruction.")
    p.add_argument("-f", "--file", default=None, help="Output file path.")
    p.add_argument("-i", "--image", action="append", default=[], help="Reference image path. Repeatable.")
    p.add_argument("-m", "--mask", default=None, help="PNG mask path for inpainting. Requires --image.")
    p.add_argument("--model", default="gpt-image-2", help="Image model.")
    p.add_argument("--size", default="1024x1024", help="1024x1024, 1536x1024, 1024x1536, auto, or alias.")
    p.add_argument("--quality", default="medium", choices=["low", "medium", "high", "auto"], help="Cost/quality dial.")
    p.add_argument("-n", "--n", type=int, default=1, help="Number of images.")
    p.add_argument("--background", choices=["auto", "opaque", "transparent"], default=None, help="Background mode.")
    p.add_argument("--format", choices=["png", "jpeg", "webp"], default="png", help="Output image format.")
    p.add_argument("--compression", type=int, default=None, help="0-100 for jpeg/webp outputs.")
    p.add_argument("--moderation", choices=["auto", "low"], default=None, help="Moderation mode when supported.")
    p.add_argument("--user", default=None, help="Optional end-user identifier.")
    return p


def normalize_args(args: argparse.Namespace) -> argparse.Namespace:
    args.size = SIZE_ALIASES.get(args.size, args.size)

    if args.n < 1:
        raise SystemExit("error: --n must be >= 1")
    if args.mask and not args.image:
        raise SystemExit("error: --mask requires at least one --image")
    if args.compression is not None:
        if args.format not in {"jpeg", "webp"}:
            raise SystemExit("error: --compression is only valid with --format jpeg or webp")
        if not 0 <= args.compression <= 100:
            raise SystemExit("error: --compression must be between 0 and 100")

    for image_path in args.image:
        if not Path(image_path).is_file():
            raise SystemExit(f"error: reference image not found: {image_path}")
    if args.mask and not Path(args.mask).is_file():
        raise SystemExit(f"error: mask file not found: {args.mask}")

    if args.file is None:
        safe_slug = "".join(c if c.isalnum() else "-" for c in args.prompt.lower())[:48].strip("-")
        args.file = str(Path("fig") / f"{safe_slug or 'image'}.{args.format}")

    return args


def output_path(base: str, index: int, total: int, fmt: str) -> Path:
    path = Path(base)
    if path.suffix:
        path = path.with_suffix(f".{fmt}")
    else:
        path = path / f"image.{fmt}"

    if total <= 1:
        return path
    return path.with_name(f"{path.stem}_{index + 1:02d}{path.suffix}")


def request_kwargs(args: argparse.Namespace) -> dict:
    kwargs = {
        "model": args.model,
        "prompt": args.prompt,
        "size": args.size,
        "quality": args.quality,
        "n": args.n,
    }
    if args.background is not None:
        kwargs["background"] = args.background
    if args.format is not None:
        kwargs["output_format"] = args.format
    if args.compression is not None:
        kwargs["output_compression"] = args.compression
    if args.moderation is not None:
        kwargs["moderation"] = args.moderation
    if args.user is not None:
        kwargs["user"] = args.user
    return kwargs


def decode_and_write(items, args: argparse.Namespace) -> list[Path]:
    written: list[Path] = []
    for index, item in enumerate(items):
        b64 = getattr(item, "b64_json", None)
        path = output_path(args.file, index, len(items), args.format)
        path.parent.mkdir(parents=True, exist_ok=True)
        if b64:
            path.write_bytes(base64.b64decode(b64))
        else:
            url = getattr(item, "url", None)
            if not url:
                raise RuntimeError("API response did not include base64 image data or URL.")
            with urllib.request.urlopen(url, timeout=120) as response:
                path.write_bytes(response.read())
        written.append(path)
    return written


def main() -> int:
    args = normalize_args(parser().parse_args())
    load_dotenv_if_available()

    if not os.environ.get("OPENAI_API_KEY"):
        print("error: OPENAI_API_KEY is not set in environment, .ai/skills/.env, .env, or ~/.env", file=sys.stderr)
        return 2

    try:
        from openai import OpenAI
    except ModuleNotFoundError:
        print("error: missing dependency 'openai'. Install with: pip install openai python-dotenv", file=sys.stderr)
        return 2

    client = OpenAI()
    kwargs = request_kwargs(args)

    try:
        if args.image:
            image_files = [open(path, "rb") for path in args.image]
            mask_file = open(args.mask, "rb") if args.mask else None
            try:
                if mask_file is not None:
                    kwargs["mask"] = mask_file
                result = client.images.edit(image=image_files, **kwargs)
            finally:
                for handle in image_files:
                    handle.close()
                if mask_file is not None:
                    mask_file.close()
        else:
            result = client.images.generate(**kwargs)

        written = decode_and_write(result.data, args)
    except Exception as exc:  # noqa: BLE001 - surface SDK/API errors to the agent/user.
        print(f"error: {exc}", file=sys.stderr)
        return 1

    for path in written:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
