from FrameGrabber import FrameGrabber
import cv2
import time

# change to local path
data_path = "D:/Repos/cale76/data/"

if __name__ == "__main__":
    grabber = FrameGrabber()
    count = 38
    
    while True:

        # press l to exit the application
        if cv2.waitKey(1) == ord('l'):
            break
        
        if time.time() - start_time >= 180:
        
            filename = data_path + "frame" + str(count) + ".png"
            frame = grabber.get_frame(resize=None)
            success = cv2.imwrite(filename, frame)
            
            if success:
                print("saved image")
            else:
                print("failed")
                
            count += 1
            start_time = time.time()

