import cv2
import numpy as np
import matplotlib.pyplot as plt

file_path = "input.jpg"
# Load the image in grayscale
image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

# Compute the histogram before equalization
hist_before = cv2.calcHist([image], [0], None, [256], [0, 256])

# Apply Histogram Equalization
equalized_image = cv2.equalizeHist(image)

# Compute the histogram after equalization
hist_after = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])

# Plot the original image and its histogram
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.plot(hist_before, color="black")
plt.title("Histogram Before Equalization")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

# Plot the equalized image and its histogram
plt.subplot(2, 2, 3)
plt.imshow(equalized_image, cmap="gray")
plt.title("Equalized Image")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.plot(hist_after, color="black")
plt.title("Histogram After Equalization")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
