import os
from PIL import Image

# Paths
input_folder = 'input'
output_folder = 'output'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process all images in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.jpg')

        # Open and process image
        with Image.open(input_path) as img:
            # Convert to RGB (JPEG does not support transparency)
            img = img.convert("RGB")

            # Optional: Resize (reduce by half)
            img = img.resize((img.width // 2, img.height // 2), Image.Resampling.LANCZOS)

            # Save as compressed JPEG
            img.save(output_path, format="JPEG", quality=40, optimize=True)

        print(f"Processed: {filename} → {output_path}")
