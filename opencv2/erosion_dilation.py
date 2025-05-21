import cv2
import numpy as np

img = cv2.imread('/Users/amakki/Documents/Coding/GitHub/'\
                 'Maksportfolio/opencv/test_image.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=3)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('dilation', img_dilation)
cv2.imwrite("dilated_output.jpg", img_dilation)

print("Dilation applied and saved as 'dilated_output.jpg'")

cv2.waitKey(0)
cv2.destroyAllWindows()  # Close the window
