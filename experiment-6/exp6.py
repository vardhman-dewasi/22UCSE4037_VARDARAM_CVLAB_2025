import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the PNG image in grayscale
image_path = "image.png"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    raise FileNotFoundError(f"Error: Unable to read the image at '{image_path}'. Please check the file path.")

# Apply Canny Edge Detection
edges_canny = cv2.Canny(image, 50, 150)

# Apply Sobel Edge Detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)  # Edges in x-direction
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)  # Edges in y-direction
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Apply Laplacian Edge Detection
edges_laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Plot the original image and edge detection results
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Medical Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(edges_canny, cmap='gray')
plt.title("Canny Edge Detection")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(sobel_combined, cmap='gray')
plt.title("Sobel Edge Detection (Combined)")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(edges_laplacian, cmap='gray')
plt.title("Laplacian Edge Detection")
plt.axis("off")

plt.tight_layout()
plt.show()