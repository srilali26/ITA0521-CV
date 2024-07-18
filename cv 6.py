import cv2
import numpy as np
cap = cv2.VideoCapture("C:/Users/User/Pictures/Camera Roll/WIN_20240718_08_41_38_Pro.mp4")
if (cap.isOpened()== False):
    print("Error opening video file")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(250) & 0xFF == ord('q'):
                break
            else:
                break
            cap.release()
            cv2.destroyAllWindows()
