import cv2
import sys

cap1 = cv2.VideoCapture("./movies/232538_tiny.mp4")
cap2 = cv2.VideoCapture("./movies/276624_tiny.mp4")

if not cap1.isOpened or not cap2.isOpened():
    print("입력 동영상 중 하나 이상을 열 수 없습니다.")
    sys.exit()

width = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)

print('너비: ', width)
print('높이: ', height)
print('FPS: ', fps1)
print('FPS: ', fps2)