import pytesseract
import cv2

# Set the Tesseract-OCR executable path (only needed on Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the image
image = cv2.imread("test_data.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale for better accuracy

# Perform OCR
text = pytesseract.image_to_string(gray)

# Save text to a file
output_file = "output.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Extracted text saved to {output_file}")