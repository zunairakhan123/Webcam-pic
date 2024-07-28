import cv2

# Initialize the webcam
cam = cv2.VideoCapture(0)

# Create a window to display the webcam feed
cv2.namedWindow("Python Webcam Screenshot App")

img_counter = 0

while True:
    # Capture frame-by-frame
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Display the resulting frame
    cv2.imshow("Python Webcam Screenshot App", frame)

    # Wait for key press
    k = cv2.waitKey(1)
    
    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing the app")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print(f"Screenshot taken and saved as {img_name}")
        img_counter += 1

# Release the webcam and destroy all windows
cam.release()
cv2.destroyAllWindows()