import cv2
path = r"C:/Users/User/Pictures/Camera Roll/WIN_20231102_12_08_18_Pro.jpg"
src = cv2.imread(path)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name, image)
cv2.waitKey(0)
