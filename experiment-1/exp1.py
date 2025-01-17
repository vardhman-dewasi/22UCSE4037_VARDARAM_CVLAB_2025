import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    print("Press 'Space' to capture an image and 'Esc' to exit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Display the webcam feed
        cv2.imshow('Webcam Feed', frame)

        # Check for user input
        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # Esc key to exit
            print("Exiting...")
            break
        elif key == 32:  # Space key to capture an image
            # Get the dimensions of the image
            height, width, channels = frame.shape
            num_pixels = height * width
            print(f"Captured image dimensions: {width}x{height}, Total pixels: {num_pixels}")

            # Save the image in JPG and PNG formats
            cv2.imwrite('captured_image.jpg', frame)
            cv2.imwrite('captured_image.png', frame)
            print("Image saved as 'captured_image.jpg' and 'captured_image.png'.")

    # Release the webcam and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
