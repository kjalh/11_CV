import cv2
import numpy as np

def on_mouse(event, x, y, flags, param):
    """
    event: 발생한 마우스 이벤트 종류 객체
    x, y: 현재 마우스 좌표
    flags: 마우스 버튼/키 상태  -> 마우스 클릭 했는지 안 했는지
    param: setMouseCallback()에서 전달할 추가 데이터  <- 이 함수 때문에 on_mouse에 파라미터가 똑같이 들어가야 됨
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"왼쪽 버튼 DOWN: ({x}, {y})")
    

img = np.full((500, 500,3), 255, dtype=np.uint8)
                #  왼쪽 상단    오른쪽 하단
cv2.rectangle(img, (50, 200), (200,300), (0, 255, 0), 3) # x = 50, y = 200 , 200 300 도 같은 (img, 좌표, 좌표, 두께, 선굵기)
cv2.rectangle(img, (300, 200), (400,300), (0, 255, 0), -1)  # -1은 색깔 채우기

                # 원의 중심, 반지름 , 색깔 , 선굵기
cv2.circle(img, (150, 400), 50, (255, 0, 0), 3)

                #          왼쪽 하단                  글꼴      폰트    색    굵기 
cv2.putText(img, "Hello", (50, 100), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,0), 1)


cv2.imshow("canvas", img)
cv2.setMouseCallback("canvas", on_mouse)

cv2.waitKey(0)
cv2.destroyAllWindows