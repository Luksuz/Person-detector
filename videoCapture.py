import cv2

cap = cv2.VideoCapture(0, cv2.CAP_ANY)

if not cap.isOpened():
    print("Error: Could not open the webcam.")

while True:
    ret, frame = cap.read()  # Read a frame
    if not ret:
        break  # Exit the loop if there's an issue reading the frame

    # Perform your computer vision processing on 'frame' here

    # Display the frame
    cv2.imshow("Webcam Feed", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
