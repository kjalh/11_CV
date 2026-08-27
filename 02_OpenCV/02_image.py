"""
cv.imread()
이미지 파일을 Numpy 배열 형태로 읽어오는 함수

cv2.IMREAD_GRAYSCALE
- 이미지를 그레이스케일로 읽어옴
- 배열의 형태는 (높이, 너비) 순서로 읽어옴

cv2.IMREAD_COLOR
- 이미지를 컬러로 읽어옴(기본값)
- 배열의 형태는 (높이, 너비, 3)가 됨
- OpenCV의 컬러 채널 순서는 BGR임

"""

import cv2

# bmp는 그림을 기본으로 저장할 수 있는 비트맵 형식의 이미지로 압축이 전혀 되지 않음
img_gray = cv2.imread("./images/dog.bmp", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("./images/dog.bmp", cv2.IMREAD_COLOR) # cv2.IMREAD_COLOR 생략 가능

print("그레이스케일 이이미 배열: ")
print(img_gray)

print()

print("컬러 이미지 배열: ")
print(img_color)

cv2.imshow('gray', img_gray)
cv2.imshow('color', img_color)
cv2.waitKey(0)
cv2.destroyAllWindows() # 창 끌 때 메모리 잡아둔 것도 할당 해제함