from FrameGrabber import FrameGrabber
import cv2

if __name__ == "__main__":
    grabber = FrameGrabber()

    while True:
        
        frame = grabber.get_frame(resize=None)
        cv2.imshow("Overwatch Frame", frame)

        if cv2.waitKey(1) == ord('q'):
            break