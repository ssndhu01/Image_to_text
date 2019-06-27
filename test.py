import pytesseract
from PIL import Image

pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tessdata\ '

text = pytesseract.image_to_string(Image.open("test.png"))
print(text)
