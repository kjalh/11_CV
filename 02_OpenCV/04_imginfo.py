import cv2
import numpy as np

img_gray = cv2.imread("./images/dog.bmp", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("./images/dog.bmp", cv2.IMREAD_COLOR)

print('img_gray type: ', type(img_gray)) # 출력: img_gray type:  <class 'numpy.ndarray'>
print('img_gray shape: ', img_gray.shape) # 출력: img_gray shape:  (364, 548)
print('img_gray dtype: ', img_gray.dtype) # img_gray dtype:  uint8

print('img_color type: ', type(img_color)) # 출력: img_color type:  <class 'numpy.ndarray'>
print('img_color shape: ', img_color.shape) # 출력: img_color shape:  (364, 548, 3)
print('img_color dtype: ', img_color.dtype) # img_color dtype:  uint8

h, w = img_color.shape[:2]
print(f'이미지 크기: {w} * {h}')

if img_color.ndim == 3:
    print('img_color는 컬러 이미지입니다.')
elif img_color.ndim == 2:
    print('img_color는 그레이스케일 이미지입니다.')

# print(img_color.ndim)
# print(img_gray.ndim)

img1 = np.zeros((240, 320, 3), dtype=np.uint8) # 가로 320, 세로 240, 컬러(검은색)

# np.empty(): 메모리 공간만 할당하고 예측할 수 없는 값을 저장함
img2 = np.empty((240, 320), dtype=np.uint8)

# full 특정 원소값으로 채워짐 여기서 120으로 설정함
img3 = np.full((240,320), 120, dtype=np.uint8)
cv2.imshow('zeros', img1)
cv2.imshow('empty', img2)
cv2.imshow('full_120', img3)  

cv2.waitKey(0)
cv2.destroyAllWindows()