import time
import cv2
from threading import Timer
from tkinter import *


def main():
    detect_face()
    interupt_activity()
    restart()


def detect_face():
    """
    Identify any faces on the screen and determine when to launch the interrupt
    :return:
    """
    global stopwatch_end
    classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # initialize thread used to reset the stopwatch
    update = Timer(0.0, reset_stopwatch)

    while True:
        # slow down frame refresh rate to help lower CPU usage
        time.sleep(0.1)

        stopwatch_end = time.time()
        _result, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = classifier.detectMultiScale(
            image=gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 255, 0), 2)

        # Detect duration a face is detected on the screen
        # len(faces) is >= 1 when face(s) detected, 0 when no face detected
        if len(faces) == 0:
            if update.is_alive():
                pass
            else:
                update = Timer(5.0, reset_stopwatch)
                update.start()
        else:
            # if a face is on screen and thread is alive, cancel the thread
            if update.is_alive():
                update.cancel()
                # sleep for 0.1s to allow thread time to finish cancel
                time.sleep(0.1)

        cv2.imshow("Faces", frame)

        if (stopwatch_end - stopwatch_start) >= 1200.0:
            break

        if cv2.waitKey(1) == ord("q"):
            quit(0)


def interupt_activity():
    """
    Blind the user and then kill the tkinter root as well as freeing the camera.
    :return:
    """
    root.after(5000, lambda: root.destroy())
    root.mainloop()
    cam.release()
    cv2.destroyAllWindows()
    restart()


def restart():
    """
    Restart the root and camera and rerun main.
    Should only ever be called from interupt_activity()
    :return:
    """
    global root, cam
    root = Tk()
    root.attributes('-fullscreen', True, '-topmost', 1)
    cam = cv2.VideoCapture(0)
    reset_stopwatch()
    main()


def reset_stopwatch():
    global stopwatch_start, stopwatch_end
    stopwatch_start, stopwatch_end = time.time(), time.time()


if __name__ == "__main__":
    root = Tk()

    cam = cv2.VideoCapture(0)
    try:
        assert cam.isOpened()
    except AssertionError:
        err_msg = Label(root, text="No Camera Detected!", font=('Arial', 50))
        err_msg.grid(row=1, column=1)
        root.mainloop()
        quit(1)

    root.attributes('-fullscreen', True, '-topmost', 1)
    stopwatch_start, stopwatch_end = time.time(), time.time()
    main()
