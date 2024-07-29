import cv2 
import numpy as np 
img = cv2.imread(r"C:\Users\SARAN\OneDrive\Pictures\HD-wallpaper-owl-eyes-owl-eyes-dark-staring-bird-black.jpg") 
rows,cols,_ = img.shape 
pts1 = np.float32([[50,50],[200,50],[50,200]]) 
pts2 = np.float32([[10,100],[200,50],[100,250]]) 
M = cv2.getAffineTransform(pts1,pts2) 
