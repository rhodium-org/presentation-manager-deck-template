"""Draws the deck's mark: three stacked slides, the front one with a line of text. Run it to remake mark.png;
replace it with your own mark (a square PNG with a transparent ground) and its alt text in idd/series/SER-0001.yml."""
from pathlib import Path

from PIL import Image, ImageDraw

S = 4                                   # drawn at four times the size, then reduced, for smooth edges
W = 600
img = Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))
d = ImageDraw.Draw(img)
ink = (255, 255, 255, 255)
for i, alpha in enumerate((90, 160, 255)):
    x, y = (70 + i * 50) * S, (110 + i * 70) * S
    d.rounded_rectangle([x, y, x + 330 * S, y + 220 * S], radius=22 * S, outline=(255, 255, 255, alpha), width=14 * S,
                        fill=(255, 255, 255, 0))
x, y = 170 * S, 250 * S
for n, w in enumerate((200, 150, 170)):
    d.rounded_rectangle([x + 40 * S, y + (50 + n * 45) * S, x + (40 + w) * S, y + (70 + n * 45) * S], radius=10 * S, fill=ink)
img.resize((W, W), Image.LANCZOS).save(Path(__file__).with_name("mark.png"))
