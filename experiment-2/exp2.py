import os
import numpy as np
import cv2

file_path = "box6_image.jpg"  # File should be in the same directory as the script

def read_image(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")
    
    # Load the image in BGR format
    image = cv2.imread(file_path)
    if image is None:
        raise ValueError(f"Unable to read the image at {file_path}.")
    return image

def scale_image(image, scale_factor):
    height, width, channels = image.shape
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    # Create a blank image with new dimensions
    scaled_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            orig_x = int(i / scale_factor)
            orig_y = int(j / scale_factor)
            scaled_image[i, j] = image[orig_x, orig_y]

    return scaled_image

def rotate_image(image, angle):
    height, width, channels = image.shape
    center_x, center_y = width // 2, height // 2
    rad = np.deg2rad(angle)

    # Create a blank canvas
    rotated_image = np.zeros_like(image)

    for i in range(height):
        for j in range(width):
            # Translate to origin
            x = j - center_x
            y = center_y - i

            # Rotate
            new_x = int(x * np.cos(rad) - y * np.sin(rad))
            new_y = int(x * np.sin(rad) + y * np.cos(rad))

            # Translate back
            new_j = new_x + center_x
            new_i = center_y - new_y

            # Check bounds
            if 0 <= new_i < height and 0 <= new_j < width:
                rotated_image[i, j] = image[new_i, new_j]

    return rotated_image

def flip_image(image, axis):
    height, width, channels = image.shape
    flipped_image = np.zeros_like(image)

    if axis == 'horizontal':
        for i in range(height):
            for j in range(width):
                flipped_image[i, j] = image[i, width - 1 - j]
    elif axis == 'vertical':
        for i in range(height):
            for j in range(width):
                flipped_image[i, j] = image[height - 1 - i, j]
    else:
        raise ValueError("Axis must be 'horizontal' or 'vertical'.")

    return flipped_image

# Main Function
if __name__ == "__main__":
    image_path = file_path  # Use the declared file path

    try:
        # Load the image
        img = read_image(image_path)
        print("Original image loaded successfully.")

        # Scaling
        scaled_img = scale_image(img, 0.5)  # Reduce size to 50%
        cv2.imwrite("scaled_image.jpg", scaled_img)
        print("Scaled image saved as 'scaled_image.jpg'.")

        # Rotation
        rotated_img = rotate_image(img, 45)  # Rotate by 45 degrees
        cv2.imwrite("rotated_image.jpg", rotated_img)
        print("Rotated image saved as 'rotated_image.jpg'.")

        # Flipping
        flipped_img = flip_image(img, 'horizontal')  # Flip horizontally
        cv2.imwrite("flipped_image.jpg", flipped_img)
        print("Flipped image saved as 'flipped_image.jpg'.")

    except ValueError as e:
        print(e)
