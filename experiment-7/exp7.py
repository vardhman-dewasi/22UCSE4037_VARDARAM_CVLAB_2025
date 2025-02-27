import cv2
import numpy as np

# Function to detect and label shapes
def detect_shapes(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detect edges using Canny
    edges = cv2.Canny(blurred, 50, 150)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Approximate the contour shape
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        
        # Get the bounding box for placing text
        x, y, w, h = cv2.boundingRect(approx)
        
        # Identify shape based on number of sides
        sides = len(approx)
        
        if sides == 3:
            shape = "Triangle"
        elif sides == 4:
            aspect_ratio = float(w) / h
            if 0.95 <= aspect_ratio <= 1.05:
                shape = "Square"
            else:
                shape = "Rectangle"
        elif sides == 5:
            shape = "Pentagon"
        elif sides > 5:
            shape = "Polygon"
        else:
            shape = "Circle"
        
        # Draw the shape and label it
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2  # Adjust size (increase for larger text)
        font_thickness = 2
        font_color = (0, 0, 255)  # BGR format — (Blue, Green, Red)

        # Draw the shape and label it
        cv2.drawContours(image, [approx], 0, (0, 255,255), 2)  # Green for contours
        cv2.putText(image, shape, (x, y + h//2), font, font_scale, font_color, font_thickness)

    return image

# Load input image
img = cv2.imread('tria.png')

# Detect and label shapes
output = detect_shapes(img)

# Display result
cv2.imshow('Shape Detection', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
