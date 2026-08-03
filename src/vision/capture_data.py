import sys  #reads what you type in the terminal 
import csv #this writes the spredsheet rile 
import cv2 #this imports the comptuer visiioon 
import mediapipe as mp 

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
CSV_PATH = "chord_data.csv"#the file everything gets saved too 


def landmarks_to_row(hand):
    row = []
    for point in hand.landmark:
        row.extend([point.x, point.y, point.z])
    return row

if __name__ == "__main__":
    chord_label = sys.argv[1]
    from src.vision.capture import open_camera
    cam = open_camera()
    saved = 0
    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        with mp_hands.Hands(max_num_hands=1) as hands:
            while True:
                ok, frame = cam.read()
                if not ok:
                    break
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = hands.process(rgb)
                if result.multi_hand_landmarks:
                    hand = result.multi_hand_landmarks[0]
                    mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
                cv2.putText(frame, f"{chord_label}: {saved}", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Collect", frame)
                key = cv2.waitKey(1)
                if key == ord(" ") and result.multi_hand_landmarks:
                    writer.writerow(landmarks_to_row(hand) + [chord_label])
                    saved += 1
                elif key == ord("q"):
                    break
    cam.release()
    cv2.destroyAllWindows()
    print(f"Saved {saved} samples for {chord_label}")