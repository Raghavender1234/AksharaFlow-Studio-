import os
from PIL import Image, ImageDraw, ImageFont

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(PROJECT_DIR, "assets")
STORE_DIR = os.path.join(ASSETS_DIR, "store_logos")
os.makedirs(STORE_DIR, exist_ok=True)


def create_keycap_icon(size=512):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Outer 3D keycap skirt (deep peacock/walnut)
    margin = int(size * 0.06)
    rad = int(size * 0.22)
    draw.rounded_rectangle(
        [margin, margin + int(size * 0.04), size - margin, size - margin],
        radius=rad,
        fill=(15, 118, 110, 255),
    )

    # Main keycap body (warm marigold-orange gradient effect)
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin - int(size * 0.05)],
        radius=rad,
        fill=(245, 158, 11, 255),
        outline=(254, 243, 199, 255),
        width=max(2, int(size * 0.02)),
    )

    # Inner keycap dish (cream/ivory)
    dish = int(size * 0.16)
    draw.rounded_rectangle(
        [dish, dish - int(size * 0.02), size - dish, size - dish - int(size * 0.07)],
        radius=int(size * 0.14),
        fill=(255, 251, 235, 255),
        outline=(217, 119, 6, 255),
        width=max(2, int(size * 0.015)),
    )

    # Draw "अ" and "A" glyph
    try:
        font_main = ImageFont.truetype("C:/Windows/Fonts/NirmalaB.ttf", int(size * 0.38))
        font_sub = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", int(size * 0.16))
    except Exception:
        font_main = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Main Devanagari 'अ' in deep peacock
    draw.text(
        (size * 0.45, size * 0.43),
        "अ",
        font=font_main,
        fill=(13, 148, 136, 255),
        anchor="mm",
    )

    # Secondary 'A' badge in coral
    draw.text(
        (size * 0.72, size * 0.26),
        "A",
        font=font_sub,
        fill=(225, 29, 72, 255),
        anchor="mm",
    )

    # Homing bar bump at bottom of keycap dish
    bar_w = int(size * 0.22)
    bar_h = max(4, int(size * 0.025))
    bx1 = (size - bar_w) // 2
    by1 = int(size * 0.72)
    draw.rounded_rectangle(
        [bx1, by1, bx1 + bar_w, by1 + bar_h],
        radius=bar_h // 2,
        fill=(217, 119, 6, 255),
    )

    return img


def main():
    base_icon = create_keycap_icon(512)
    ico_path = os.path.join(ASSETS_DIR, "aksharaflow.ico")
    base_icon.save(
        ico_path,
        format="ICO",
        sizes=[(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)],
    )
    print(f"Created icon: {ico_path}")

    # Save Microsoft Store Partner Center PNG Logos
    for s, name in [
        (300, "StoreLogo_300x300.png"),
        (150, "Square150x150Logo.png"),
        (310, "Square310x310Logo.png"),
    ]:
        resized = base_icon.resize((s, s), Image.Resampling.LANCZOS)
        resized.save(os.path.join(STORE_DIR, name), format="PNG")

    print(f"Created Microsoft Store logos in: {STORE_DIR}")


if __name__ == "__main__":
    main()
