import cv2
import numpy as np
import matplotlib.pyplot as plt

def high_pass_filter(image, radius):
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2

    mask = np.ones((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), radius, 0, -1)

    return mask

def low_pass_filter(image, radius):
    rows, cols = image.shape
    crow, ccol = rows // 2, cols // 2

    mask = np.zeros((rows, cols), np.uint8)
    cv2.circle(mask, (ccol, crow), radius, 1, -1)

    return mask

# Read the image in grayscale
image = cv2.imread("input.jpg", cv2.IMREAD_GRAYSCALE)

# Perform Fourier Transform
dft = np.fft.fft2(image)
dft_shift = np.fft.fftshift(dft)

# Apply high-pass filter
hp_filter = high_pass_filter(image, 30)
high_passed = dft_shift * hp_filter
high_passed_image = np.abs(np.fft.ifft2(np.fft.ifftshift(high_passed)))

# Apply low-pass filter
lp_filter = low_pass_filter(image, 30)
low_passed = dft_shift * lp_filter
low_passed_image = np.abs(np.fft.ifft2(np.fft.ifftshift(low_passed)))

# Save the images
cv2.imwrite("high_passed.jpg", high_passed_image)
cv2.imwrite("low_passed.jpg", low_passed_image)

# Display the images
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title("Original Image")
plt.imshow(image, cmap="gray")

plt.subplot(1, 3, 2)
plt.title("High-Passed Image")
plt.imshow(high_passed_image, cmap="gray")

plt.subplot(1, 3, 3)
plt.title("Low-Passed Image")
plt.imshow(low_passed_image, cmap="gray")

plt.show()
