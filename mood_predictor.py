import os
import cv2
import warnings
from fer import FER
from datetime import datetime
import pandas as pd

# ===============================#
#      CONFIGURATION SECTION     #
# ===============================#

# Hide TensorFlow logs and suppress warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 3 = Only Errors
warnings.filterwarnings("ignore", category=UserWarning)

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("[❌] Cannot access the webcam. Check if it's connected or used by another app.")

# Initialize FER detector with MTCNN
detector = FER(mtcnn=True)

# Initialize mood log
log_data = []

print("[✅] Real-time Mood Detection Started (Press 'q' to quit)")

# ===============================#
#      MAIN LOOP STARTS HERE     #
# ===============================#
while True:
    ret, frame = cap.read()
    if not ret:
        print("[❌] Failed to capture frame. Exiting loop.")
        break

    # Detect emotions
    results = detector.detect_emotions(frame)

    for face in results:
        (x, y, w, h) = face["box"]
        emotions = face["emotions"]

        # Identify top emotion
        top_emotion = max(emotions, key=emotions.get)
        confidence = emotions[top_emotion]

        # Draw bounding box & label
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 200, 0), 2)
        cv2.putText(frame, f"{top_emotion} ({confidence:.2f})", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 200, 0), 2)

        # Save to log
        log_data.append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "emotion": top_emotion,
            "confidence": round(confidence, 2)
        })

    # Display window
    cv2.imshow("🧠 Mood Detection", frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("\n[🔒] Exit key pressed. Closing app...")
        break

# ===============================#
#        CLEANUP & LOGGING       #
# ===============================#

cap.release()
cv2.destroyAllWindows()
print("[✅] Webcam feed closed.")

# Save mood log to CSV
if log_data:
    df = pd.DataFrame(log_data)
    df.to_csv("mood_log.csv", index=False)
    print("[💾] Mood data saved to: mood_log.csv")
else:
    print("[ℹ️] No mood data to save.")
