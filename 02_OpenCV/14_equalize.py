import cv2
import matplotlib.pyplot as plt

img_gray = cv2.imread("./images/Hawkes.jpg", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("./images/field.bmp")

cv2.imshow("gray original", img_gray)
cv2.imshow("color original", img_color)
img = cv2.equalizeHist(img_gray)
cv2.imshow("img", img)

"""
normalize()
- 정규화
- 값의 범위 조정
- 최솟값/최댓값
- 기본적으로 비율을 유지하며 변화
- 대비 개선이 주목적은 아님

"""

cv2.waitKey(0)
cv2.destroyAllWindows()
