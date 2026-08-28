import cv2
import sys

capin = cv2.VideoCapture(0)

# if not capin.isOpened():
#     print('카메라를 열 수 없습니다.')
#     sys.exit()

# print('카메라 연결 성공!')


# while True:
#     ret, frame = capin.read()
#     if not ret:
#         print('카메라 프레임을 읽지 못했습니다.')
#         break
#     cv2.imshow('camera', frame)
#     if cv2.waitKey(1) == 27:
#         cv2.destroyAllWindows()
#         break


width = int(capin.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capin.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = capin.get(cv2.CAP_PROP_FPS)

# print('너비: ', width)
# print('높이: ', height)
# print('FPS: ', fps)


fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("myvideo.avi", fourcc, fps, (width, height))

if not out.isOpened():
    capin.release()
    raise RuntimeError("출력 동영상 파일을 생성할 수 없습니다.")

delay = max(1, round(1000/fps))
stop = False


while True:
    ret, frame = capin.read()
    if not ret:
        break

    if frame.shape[1] != width or frame.shape[0] != height:
        frame = cv2.resize(frame, (width, height))

    out.write(frame)

    cv2.imshow('output', frame)

    if cv2.waitKey(delay) == 27:
        stop = True
        break


# capin.release()

cv2.destroyAllWindows()