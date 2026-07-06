import cv2
import easyocr
import os

IMAGE_PATH = "images/car.jpg"
OUTPUT_PATH = "output/plate.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Image not found. Please check the image path.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 200)

contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:20]

plate_image = None

for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)

        if 2.0 < aspect_ratio < 6.0:
            plate_image = image[y:y+h, x:x+w]
            cv2.imwrite(OUTPUT_PATH, plate_image)
            break

if plate_image is None:
    print("License plate could not be detected.")
    exit()

reader = easyocr.Reader(['en'])
result = reader.readtext(plate_image)

plate_text = ""

for detection in result:
    plate_text += detection[1] + " "

print("Recognized License Plate:", plate_text.strip())
print("Cropped plate image saved to:", OUTPUT_PATH)