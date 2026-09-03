import cv2

"""
윤곽선(Contour)
객체의 바깥 경계선을 이루는 좌표들의 집합
"""

img = cv2.imread("./images/contours.bmp", cv2.IMREAD_GRAYSCALE)
milkdrop = cv2.imread("./images/milkdrop.bmp", cv2.IMREAD_GRAYSCALE)

_, img_bin = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
_, milk_bin = cv2.threshold(milkdrop, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

