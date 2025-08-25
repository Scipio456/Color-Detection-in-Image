
import cv2
import numpy as np

# Read the input image
img = cv2.imread('Blue_Lamborgini.jpg')  # Replace with your image path
img = cv2.resize(img, (600, 400))      # Optional: resize for better viewing

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define HSV range for blue color
lower_blue = np.array([90, 60, 50])
upper_blue = np.array([140, 255, 255])


# Create a binary mask where blue colors are white
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply the mask to extract the blue parts
result = cv2.bitwise_and(img, img, mask=mask)

# Display the original image, mask, and result
cv2.imshow('Original Image', img)
cv2.imshow('Blue Mask', mask)
cv2.imshow('Detected Blue Color', result)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Run
#EVM: source ~/color-env/bin/activate
#compile and run: python3 color_detection.py
