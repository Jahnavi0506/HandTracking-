This project demonstrates real-time hand tracking using OpenCV and MediaPipe in Python. It captures video from a webcam and detects multiple hands with landmarks in real-time. 

🛠️ Features
Uses MediaPipe Hands solution for landmark detection.

Real-time webcam video capture using OpenCV.

Draws hand landmarks and connections between them.

Tracks and prints the pixel coordinates of each landmark.

Highlights the thumb tip (landmark ID 4) with a filled circle.

Calculates and displays the frames per second (FPS) on screen.

📷 Sample Output
Display window shows live video with hand landmarks.

Thumb tip is shown with a purple circle.

FPS displayed on the top-left corner.


🧠 How it Works
Converts the webcam frame to RGB (required for MediaPipe).

Processes each frame to detect hand landmarks.

Converts normalized landmark coordinates to pixel values.

Visualizes the landmarks using cv2.circle() and draw_landmarks().

📦 Dependencies
Python 3.x

opencv-python

mediapipe

>Press 'q' to quit the program.
