import numpy as np
kernel = np.ones((5,5), np.uint8)
print(kernel)
path = r"C:\Users\SARAN\OneDrive\Pictures\HD-wallpaper-owl-eyes-owl-eyes-dark-staring-bird-black.jpg"
img =cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny-cv2.Canny(imgBlor,100,200) 
imgDilation = cv2.dilateCimg(annykemel, iterations = 10)
imgEroded = cv2.erode(imgDilation,kernel,iterations=2)
cv2.imshow("Img Erosion",imgEroded)
Ev2.waitKey(0)
