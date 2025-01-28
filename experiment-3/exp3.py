import cv2
import numpy as np

def adjust_parameters(val):
    pass

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create a window for the trackbars
cv2.namedWindow("Adjust Parameters")

# Create trackbars for each parameter
cv2.createTrackbar("Contrast", "Adjust Parameters", 10, 20, adjust_parameters)
cv2.createTrackbar("Brightness", "Adjust Parameters", 50, 100, adjust_parameters)
cv2.createTrackbar("Sharpness", "Adjust Parameters", 0, 10, adjust_parameters)
cv2.createTrackbar("Hue", "Adjust Parameters", 0, 180, adjust_parameters)
cv2.createTrackbar("Saturation", "Adjust Parameters", 50, 100, adjust_parameters)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Get values from trackbars
    contrast = cv2.getTrackbarPos("Contrast", "Adjust Parameters") / 10
    brightness = cv2.getTrackbarPos("Brightness", "Adjust Parameters") - 50
    sharpness = cv2.getTrackbarPos("Sharpness", "Adjust Parameters")
    hue = cv2.getTrackbarPos("Hue", "Adjust Parameters")
    saturation = cv2.getTrackbarPos("Saturation", "Adjust Parameters") / 50

    # Adjust contrast and brightness
    frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

    # Convert to HSV for hue and saturation adjustment
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 0] = (hsv[:, :, 0] + hue) % 180  # Adjust hue
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * saturation, 0, 255)  # Adjust saturation
    frame = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

    # Apply sharpness adjustment
    if sharpness > 0:
        kernel = np.array([[-1, -1, -1],
                           [-1, 9 + sharpness, -1],
                           [-1, -1, -1]])
        frame = cv2.filter2D(frame, -1, kernel)

    # Show the adjusted frame
    cv2.imshow("Webcam", frame)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
