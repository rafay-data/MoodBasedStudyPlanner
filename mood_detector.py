import cv2
import sys
import time

def load_haarcascade(path="haarcascade_frontalface_default.xml"):
    cascade = cv2.CascadeClassifier(path)
    if cascade.empty():
        print("[❌] Failed to load Haarcascade XML file.")
        sys.exit()
    print("[📂] Haarcascade loaded successfully.")
    return cascade

def initialize_webcam(camera_index=0, width=640, height=480):
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("[❌] Could not access webcam.")
        sys.exit()
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    print("[🎥] Webcam initialized.")
    return cap

def detect_faces(cascade, gray_frame):
    faces = cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )
    return faces

def draw_faces(frame, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
        cv2.putText(frame, "Face", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

def display_fps(frame, fps):
    cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

def main():
    print("[✅] Starting Face Detection Application...")
    face_cascade = load_haarcascade()
    cap = initialize_webcam()

    prev_time = time.time()
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[❌] Failed to capture frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detect_faces(face_cascade, gray)

        draw_faces(frame, faces)
        frame_count += 1

        # Calculate and display FPS every 10 frames
        if frame_count >= 10:
            curr_time = time.time()
            fps = frame_count / (curr_time - prev_time)
            prev_time = curr_time
            frame_count = 0
        else:
            fps = 0

        display_fps(frame, fps)
        cv2.imshow("🎯 Real-Time Face Detection", frame)

        key = cv2.waitKey(1)
        if key & 0xFF == ord("q"):
            print("[🔒] Exiting application on user request.")
            break

    cap.release()
    cv2.destroyAllWindows()
    print("[✅] Webcam released and all windows closed.")

if __name__ == "__main__":
    main()
