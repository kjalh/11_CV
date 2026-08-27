import cv2
import sys

cap = cv2.VideoCapture("./movies/232538_tiny.mp4")

if not cap.isOpened():
    print('동영상을 불러올 수 없습니다.')
    sys.exit()

print('동영상 로드 성공!')

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

print('너비: ', width)
print('높이: ', height)
print('프레임 수: ', frame_count)
print('FPS: ', fps)