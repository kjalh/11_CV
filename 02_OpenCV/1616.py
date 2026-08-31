import cv2
import sys

sea = cv2.VideoCapture("./movies/sea.mp4")
girl = cv2.VideoCapture("./movies/woman.mp4")



if not sea.isOpened or not girl.isOpened():
    print("입력 동영상 중 하나 이상을 열 수 없습니다.")
    sys.exit()


width = int(sea.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(sea.get(cv2.CAP_PROP_FRAME_HEIGHT))
sea_fps = sea.get(cv2.CAP_PROP_FPS)
girl_fps = girl.get(cv2.CAP_PROP_FPS)

delay = max(1, round(1000/sea_fps))

while True:
    hsv = cv2.cvtColor(girl, cv2.COLOR_BGR2HSV)

    lower_green = (40, 150, 0)
    upper_green = (80, 255, 255)

    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    green_mask.release()

    if cv2.waitKey(delay) == 27:
                stop = True
                break

cv2.waitKey(0)
cv2.destroyAllWindows()

# gril_only = cv2.copyTo(sea, mask)









