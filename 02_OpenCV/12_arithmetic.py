import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("./images/dog.jpg")
img2 = cv2.imread("./images/square.bmp") 

# 1. 단순 덧셈. 255보다 큰 값은 255로 제한
dst_add = cv2.add(img1, img2)

# 2. 가중치 합성
# img1 * 0.5 + img2 * 0.5 + ?
dst_blend = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# 3. 뺄셈. 음수가 되는 값은 0으로 제한
dst_subtract = cv2.subtract(img1, img2)

