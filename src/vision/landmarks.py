import cv2 #this opens the CV camera and image handling 
import mediapipe as mp #this is googles ml tookkit named mp 

mp_hands = mp.solutions.hands #thisi sshqwat grabs the hand tracking and just gives it  a shrt name with a varible. 
mp_draw = mp.solutions.drawing_utils #this is medipipes drawing which helps wiht paiting the dotcs and conencting luines onto an image 

if __name__ == "__main__":
    from src.vision.capture import open_camera #this is from the vision camera 

    cam = open_camera() #this opens up the camera 

    with mp_hands.Hands(max_num_hands = 1 ) as hands: #this is what starts up the program 
        #the reaosn max_num_hand is 1 is because i only have one freetting hadns 
        while True: #while the video frame is in loop 
            ok, frame = cam.read() #this grabs one frame and returns two things a success flag and the image itsel s
            if not ok:
                break # camera filed or ended mean get out 
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #this opens the cv and stores the color blue rreen and red
            result = hands.process(rgb) #this looks at the image and returns wtv is found 
            if result.multi_hand_landmarks: #if no hands found skipp the drawing 
                for hand in result.multi_hand_landmarks: #this lopps over found hands 
                    mp_draw.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)
            cv2.imshow("Hands", frame) #shows the annoptated frame 
            if cv2.waitKey(1) == ord("q"): #usese keyboard q to quit 
                break
        cam.release()
        cv2.destroyAllWindows() #lets go of the cmaera and closes the iwnod 