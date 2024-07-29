import cv2
cap = cv2.VideoCapture(0)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS) import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)
print(kernel) 
path = r"C:\Users\SARAN\OneDrive\Pictures\HD-wallpaper-owl-eyes-owl-eyes-dark-staring-bird-black.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
cv2.imshow("Img Canny",imgCanny) 
cv2.waitKey(0) 
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output = cv2.VideoWriter(r"C:\Users\SARAN\Downloads\37006-413208203_small.mp4", fourcc, 2,(width, height))
while True: 
 	ret, frame = cap.read()
 	cv2.imshow("frame", frame) 
 
 	output.write(frame)
 	k = cv2.waitKey(24)
 	if k == ord("q"): 
 	 	break 
cap.release()
output.release()
cv2.destroyAllWindows() 
