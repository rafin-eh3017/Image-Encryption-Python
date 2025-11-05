# Prodigy InfoTech - Task 2
# Pixel Manipulation for Image Encryption
# Author: Rafin

import argparse
from pathlib import Path
from PIL import Image
import sys
import hashlib

def xor_encrypt_decrypt(img: Image.Image, key: int) -> Image.Image:
    """XOR each RGB channel with the given key (0-255). Reversible."""
    if img.mode not in ("RGB", "RGBA", "L"):
        img = img.convert("RGBA" if "A" in img.getbands() else "RGB")

    has_alpha = img.mode == "RGBA"
    pixels = img.load()
    w, h = img.size

    for y in range(h):
        for x in range(w):
            px = pixels[x, y]
            if has_alpha:
                r, g, b, a = px
                pixels[x, y] = (r ^ key, g ^ key, b ^ key, a)
            elif img.mode == "RGB":
                r, g, b = px
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)
            else: # L (grayscale)
                (l,) = (px,) if isinstance(px, int) else px
                pixels[x, y] = l ^ key
    return img

def swap_encrypt_decrypt(img: Image.Image) -> Image.Image:
    """Swap R <-> B channels (apply twice to restore)."""
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGB")
    r, g, b, *rest = img.split() + [None, None] # pad
    swapped = Image.merge("RGB", (b, g, r)) if img.mode == "RGB" else Image.merge("RGBA", (b, g, r, img.split()[3]))
    return swapped

def hash_file(path: Path) -> str:
    """Return SHA256 of a file for quick 'same file' check."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def parse_args():
    p = argparse.ArgumentParser(
        description="Image encryption/decryption via pixel manipulation (xor/swap)."
    )
    p.add_argument("--mode", choices=["encrypt", "decrypt"], required=True, help="Operation to perform.")
    p.add_argument("--method", choices=["xor", "swap"], default="xor", help="Pixel manipulation method.")
    p.add_argument("--input", "-i", required=True, help="Path to input image (jpg/png).")
    p.add_argument("--output", "-o", required=True, help="Path to output image.")
    p.add_argument("--key", type=int, default=123, help="XOR key (0-255). Only used for method=xor.")
    return p.parse_args()

def main():
    args = parse_args()
    inp = Path(args.input)
    outp = Path(args.output)

    if not inp.exists():
        print(f"[ERROR] Input not found: {inp}", file=sys.stderr)
        sys.exit(1)

    if args.method == "xor" and not (0 <= args.key <= 255):
        print("[ERROR] --key must be between 0 and 255 for XOR.", file=sys.stderr)
        sys.exit(1)

    img = Image.open(inp)

    if args.method == "xor":
        processed = xor_encrypt_decrypt(img.copy(), args.key)
    else: # swap
        processed = swap_encrypt_decrypt(img.copy())

    # Always save as PNG to avoid JPEG compression artifacts in demos
    outp = outp.with_suffix(".png")
    processed.save(outp)

    print(f"[OK] {args.mode.title()} complete using method={args.method} -> {outp}")

if __name__ == "__main__":
    main()
