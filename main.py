from PIL import Image
import pytesseract
import numpy as np
import cv2

filename = 'codeAdaPlain.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)

image = cv2.imread('color.jpg', 0)


thresh = cv2.threshold(
    image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Remove horizontal lines
horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
detect_horizontal = cv2.morphologyEx(
    thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
cnts = cv2.findContours(
    detect_horizontal, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cv2.fillPoly(thresh, cnts, [0, 0, 0])

# Remove vertical lines
vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 45))
detect_vertical = cv2.morphologyEx(
    thresh, cv2.MORPH_OPEN, vertical_kernel, iterations=2)
cnts = cv2.findContours(
    detect_vertical, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cv2.fillPoly(thresh, cnts, [0, 0, 0])

result = 255 - thresh

data = pytesseract.image_to_string(result, lang='eng')
print(data)

# cv2.imshow('thresh', thresh)
# cv2.imshow('result', result)
# cv2.waitKey()
