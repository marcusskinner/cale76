from FrameGrabber import FrameGrabber
import cv2
import time

data_path = "D:/Repos/overwatch_bot/data/"

if __name__ == "__main__":
    grabber = FrameGrabber()

    count = 4
    while True:
        filename = data_path + "frame" + str(count) + ".png"
        print(filename)
        frame = grabber.get_frame(resize=None)
        success = cv2.imwrite(filename, frame)
        if success:
            print("saved image")
        else:
            print("failed")
            
        count += 1
        time.sleep(180)