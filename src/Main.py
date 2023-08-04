import cv2


# read from camera
def start_camera():
    cap = cv2.VideoCapture(0)   # 0 - default 1 camera, else give id to display that particular camera
    while True:
        success, vid = cap.read()
        cv2.imshow("Video", vid)
        # display the video until 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    print("Welcome to Number plate detection project")

    start_camera()
