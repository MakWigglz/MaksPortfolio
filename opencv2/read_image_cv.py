# cv2 imread (/Users/amakki/Documents/Coding-Design/GitHub/Maksportfolio/opencv/test_image.jpg)
import cv2
img = cv2.imread("test_image.jpg", cv2.IMREAD_COLOR)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
