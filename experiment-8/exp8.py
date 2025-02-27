import cv2
import numpy as np

# Load the input image
image = cv2.imread('image.png')

# Add a watermark
watermark_text = 'WATERMARK'
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
font_thickness = 3
color = (0, 0, 255)  # Red color for watermark

# Get the size of the text
(text_width, text_height), _ = cv2.getTextSize(watermark_text, font, font_scale, font_thickness)

# Set position for watermark (center of the image)
x = (image.shape[1] - text_width) // 2
y = (image.shape[0] + text_height) // 2

# Draw the watermark
watermarked_image = image.copy()
cv2.putText(watermarked_image, watermark_text, (x, y), font, font_scale, color, font_thickness)

# Save and display watermarked image
# cv2.imwrite('watermarked_image.png', watermarked_image)
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Remove the watermark using inpainting
# Create a mask for the watermark
mask = np.zeros_like(image[:, :, 0])
cv2.putText(mask, watermark_text, (x, y), font, font_scale, 255, font_thickness)

# Inpainting to remove watermark
inpainted_image = cv2.inpaint(watermarked_image, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

# Save and display the result
# cv2.imwrite('inpainted_image.png', inpainted_image)
cv2.imshow('Inpainted Image', inpainted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
