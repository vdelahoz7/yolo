import cv2
import mediapipe as mp

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

def video():
    cap = cv2.VideoCapture(1)

    holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

    while cap.isOpened():
        status, frame = cap.read()

        if not status:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = holistic.process(rgb_frame)

        print(f"LEFT HAND:")
        print(results.left_hand_landmarks)

        cv2.imshow("frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()


if __name__ == '__main__':
    video()