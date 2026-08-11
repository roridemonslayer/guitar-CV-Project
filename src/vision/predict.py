import pickle 
import time
from collections import deque, Counter

history = deque(maxlen=10)

MODEL_PATH = "chord_model.pkl"

def load_model():
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

def get_vision_verdict(model, hand): #this loads the model and my hands
    from src.vision.training import normalize #this is getting ht emath 
    row = [] 
    for point in hand.landmark: #this takes 21 points. into  63 numbers 
        row.extend([point.x, point.y, point.z])
    row = normalize(row)

    probabilities = model.predict_proba([row])[0]
    best_index = probabilities.argmax() #which postion holds the same argmax 

    return {
        "chord_shape": model.classes_[best_index],
        "confidence":float(probabilities[best_index]),
        "timestamp": time.time(),
    }
if __name__ == "__main__":
    import cv2
    import mediapipe as mp
    from src.vision.capture import open_camera

    mp_hands = mp.solutions.hands
    model = load_model()
    cam = open_camera()

    with mp_hands.Hands(max_num_hands=1) as hands:
        while True:
            ok, frame = cam.read()
            if not ok:
                break
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(rgb)
            if result.multi_hand_landmarks:
                verdict = get_vision_verdict(model, result.multi_hand_landmarks[0])
                label = f"{verdict['chord_shape']} {verdict['confidence']:.2f}"
                cv2.putText(frame, label, (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Predict", frame)
            if cv2.waitKey(1) == ord("q"):
                break
    cam.release()
    cv2.destroyAllWindows()