import cv2
import easyocr
import os

IMAGE_PATH = "images/car.jpg"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("Image not found. Please check the image path.")
    exit()

original = image.copy()

# 1. Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("output/grayscale.jpg", gray)

# 2. Blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imwrite("output/blur.jpg", blurred)

# 3. Edge Detection
edges = cv2.Canny(blurred, 50, 200)
cv2.imwrite("output/edges.jpg", edges)

# 4. Contour Detection
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
            plate_image = original[y:y+h, x:x+w]
            cv2.imwrite("output/plate.jpg", plate_image)

            detected_image = original.copy()
            cv2.rectangle(detected_image, (x, y), (x + w, y + h), (0, 255, 0), 3)
            cv2.imwrite("output/detected_plate.jpg", detected_image)
            break

if plate_image is None:
    print("License plate could not be detected.")
    exit()

# 5. OCR
reader = easyocr.Reader(['en'])
result = reader.readtext(plate_image)

plate_text = ""

for detection in result:
    plate_text += detection[1] + " "

print("Recognized License Plate:", plate_text.strip())
print("Saved grayscale image: output/grayscale.jpg")
print("Saved blur image: output/blur.jpg")
print("Saved edge image: output/edges.jpg")
print("Saved detected plate image: output/detected_plate.jpg")
print("Saved cropped plate image: output/plate.jpg")