import cv2

def open_camera():
    return cv2.VideoCapture(0)

if __name__ == "__main__":
    cam = open_camera()
    print("Press q to quit")
    while True:
        ok, frame = cam.read()
        if not ok:
            break
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord("q"):
            break
    cam.release()
    cv2.destroyAllWindows()