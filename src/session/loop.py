import time
import cv2 
import mediapipe as mp 


from src.shared.models import example_chord_chart #the song to play
from src.session.scorer import is_chord_correct #the judget 
from src.vision.predict import load_model, get_vision_verdict, smooth #the cam
from src.sound.pitch import get_sound_verdict #ythe mic 
from src.vision.capture import open_camera # the cam opener

TIMEOUT = 15.0 #sec per chord before it moves on 

mp_hands = mp.solutions.hands #the hand model 

if __name__ ==  "__main__":
    model = load_model()
    cam  = open_camera() #this opens up the camera 

    for num in [3,2,1]:
        print(num)
        time.sleep(1) #one beat the time
    print("GO!")

    with mp_hands.Hands(max_num_hands = 1) as hands: #start hands tracking 
        for entry in example_chord_chart["sequence"]: #goes chord by chord 
            target = entry["chord"] #t5he chord ur supposed to play
            print(f"play: {target}")
            started = time.time() #time stamp for the chord
            got_it = False

            while time.time() - started < TIMEOUT: #keep goingm till the 5 sec time is out 
                ok, frame = cam.read() #grabs one frame
                if not ok:
                    break #cam breakl 
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = hands.process(rgb) #this finds the hands 

                if result.multi_hand_landmarks: #only judges if hands are visible
                    vision = get_vision_verdict(model, result.multi_hand_landmarks[0]) #thsi is the cam opinio 
                    vision["chord_shape"] = smooth(vision["chord_shape"])#this is the flicker filter
                    sound = get_sound_verdict() #this gets the mics opiniomn
                    print(vision["chord_shape"], vision["confidence"], "|", sound["sound_pick_up"], sound["confidence"], sound["volume"])

                    if is_chord_correct(target, vision, sound):
                        got_it = True
                cv2.putText(frame, f"Play: {target}", (10,40), #target chord
                            cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                cv2.imshow("Game", frame)
                cv2.waitKey(1)
                if got_it:
                    break
            print("Correct!" if got_it else "Missed." ) #why the loop ended
    cam.release()
    cv2.destroyAllWindows() #cksie the windows
