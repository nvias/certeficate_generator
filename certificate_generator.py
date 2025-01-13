import os
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

TEMPLATE_DIR = "source_cert"  # Directory to store uploaded certificate templates
OUTPUT_DIR = "certificates"  # Directory to store generated certificates
FONT_PATH = "fonts/Rajdhani-SemiBold.ttf"

# Default dimensions for A4 landscape in pixels (300 DPI)
A4_WIDTH = 3508
A4_HEIGHT = 2480

def font(size):
    """Load font with the specified size."""
    return ImageFont.truetype(FONT_PATH, size=size)

def generate_certificate(name, template_path, standing=None):
    """
    Generate a certificate with the given name and optional standing.
    Ensures compatibility with A4 landscape templates.
    """
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)
    W, H = image.width, image.height

    # Scale settings based on A4 landscape
    name_font_size = int(W * 0.05)  # Name font size: 5% of width
    standing_font_size = int(name_font_size * 0.8)  # Standing font size: 80% of name font size
    name_height_offset = int(H * 0.3)  # Place name about 30% from the top
    standing_height_offset = int(H * 0.4)  # Place standing slightly below the name

    # Draw name
    name_font = font(name_font_size)
    name_width, name_height = draw.textsize(name, font=name_font)
    name_x = (W - name_width) / 2
    name_y = name_height_offset
    draw.text((name_x, name_y), name, fill="black", font=name_font)

    # Draw standing if provided
    if standing:
        standing_font = font(standing_font_size)
        standing_width, standing_height = draw.textsize(standing, font=standing_font)
        standing_x = (W - standing_width) / 2
        standing_y = standing_height_offset
        draw.text((standing_x, standing_y), standing, fill="black", font=standing_font)

    # Save certificate
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    output_path = os.path.join(OUTPUT_DIR, f"certificate_{name}.png")
    image.save(output_path)
    return output_path

def list_templates():
    """List available certificate templates."""
    if not os.path.exists(TEMPLATE_DIR):
        os.makedirs(TEMPLATE_DIR)
    return [os.path.join(TEMPLATE_DIR, file) for file in os.listdir(TEMPLATE_DIR) if file.endswith(('.png', '.jpg'))]

if __name__ == "__main__":
    # Example usage
    templates = list_templates()
    if templates:
        print(f"Using template: {templates[0]}")
        generate_certificate("John Doe", templates[0], standing="1st")
    else:
        print("No templates found. Please upload a template to the templates directory.")
