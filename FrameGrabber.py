import mss
import cv2
import numpy as np

class FrameGrabber:
    
    def __init__(self, width=2560, height=1440):
        self.sct = mss.mss()
        monitors = self.sct.monitors
        self.monitor = monitors[1]
        
    def get_frame(self, resize=(640, 640)):
        frame = np.array(self.sct.grab(self.monitor))[:, :, :3] 
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        if resize:
            frame = cv2.resize(frame, resize)
            
        return frame
