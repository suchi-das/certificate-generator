from PIL import Image, ImageDraw, ImageFont
import os

TEMPLATE_PATH = "template_cert.jpg"
FONT_PATH = "font_temp.ttf"
OUTPUT_FOLDER = "generated_certs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

FONT_SIZE = 100
font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

NAME_COORDS = (500, 1000)
COURSE_COORDS = (500, 1100)
DATE_COORDS = (500, 1200)

with open("names_temp.txt", "r", encoding="utf-8") as file:
    for line in file:
        if not line.strip():
            continue

        parts = [i.strip() for i in line.strip().split(",")]

        if len(parts) != 3:
            print(f"Skipping invalid line: {line}")
            continue

        name, course, date = parts

        image = Image.open(TEMPLATE_PATH).convert("RGB")
        draw = ImageDraw.Draw(image)

        draw.text(NAME_COORDS, name, fill="white", font=font)
        draw.text(COURSE_COORDS, course, fill="white", font=font)
        draw.text(DATE_COORDS, date, fill="white", font=font)

        filename = f"{name.replace(' ', '_')}_certificate.jpg"
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        image.save(output_path)

        print(f"Generated: {filename}")
