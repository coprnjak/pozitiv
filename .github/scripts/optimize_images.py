"""Smanjuje JPEG fotografije u mapi images/ za web.

- duža strana najviše 2500 px
- JPEG kvaliteta 85, progresivno, s ICC profilom i EXIF podacima
- fotografija se mijenja samo ako se smanji ili ako nova verzija
  ima barem 15 % manje bajtova (tako se ista fotka ne komprimira
  iznova pri svakom pokretanju)
"""
import io
import sys
from pathlib import Path

from PIL import Image, ImageOps

MAX_SIDE = 2500
QUALITY = 85
MIN_SAVING = 0.15
ORIENTATION = 0x0112


def optimize(path: Path) -> bool:
    original = path.read_bytes()
    try:
        im = Image.open(io.BytesIO(original))
        im.load()
    except Exception as exc:  # oštećena ili neobična datoteka
        print(f"preskačem {path}: {exc}")
        return False

    if im.mode not in ("RGB", "L"):
        print(f"preskačem {path}: način boja {im.mode}")
        return False

    icc = im.info.get("icc_profile")
    exif = im.getexif()
    orientation = exif.get(ORIENTATION, 1)
    forced = False

    if orientation != 1:
        im = ImageOps.exif_transpose(im)
        exif[ORIENTATION] = 1
        forced = True

    if max(im.size) > MAX_SIDE:
        im.thumbnail((MAX_SIDE, MAX_SIDE), Image.LANCZOS)
        forced = True

    options = dict(quality=QUALITY, optimize=True, progressive=True)
    if icc:
        options["icc_profile"] = icc
    if len(exif):
        options["exif"] = exif.tobytes()

    buffer = io.BytesIO()
    im.save(buffer, "JPEG", **options)
    smaller = buffer.getvalue()

    if forced or len(smaller) <= len(original) * (1 - MIN_SAVING):
        path.write_bytes(smaller)
        print(f"{path}: {len(original) // 1024} KB -> {len(smaller) // 1024} KB, {im.size[0]}x{im.size[1]}")
        return True
    return False


def main() -> None:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "images")
    files = [p for p in sorted(root.rglob("*")) if p.suffix.lower() in (".jpg", ".jpeg")]
    changed = sum(optimize(p) for p in files)
    print(f"pregledano {len(files)}, smanjeno {changed}")


if __name__ == "__main__":
    main()
