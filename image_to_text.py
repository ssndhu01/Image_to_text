import cv2
import pytesseract
import os
from PIL import Image
import numpy as np


# Arguments from terminal or command prompt 
from sys import argv

if len(argv)<1:
    print("Format: python image_to_text.py path-of-image")
else:
    print('*** Start recognize text from image ***')

# Recognize text with tesseract for python 

# Path of the Tessdata folder where your tesseract OCR is installed or build
pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\Tessdata\ '
for i in range(1,len(argv)):
    img = cv2.imread(i)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("temp.png", img)
    # Tesseract is called to convert image to String from given Image
    text = pytesseract.image_to_string(Image.open("temp.png"))
    os.remove("temp.png")
    print(text)
