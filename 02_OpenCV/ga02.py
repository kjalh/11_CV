import cv2
import numpy as np

def nothing(x):
    # 트랙바 콜백 함수 (아무 작업도 하지 않음)
    pass

# 1. 이미지 불러오기 (여기에 테스트할 이미지 경로를 입력하세요)
# 이미지가 같은 폴더에 없다면 절대 경로를 입력해야 합니다.
image_path = './images/park.png' 
original_img = cv2.imread(image_path)

# 이미지를 정상적으로 불러왔는지 확인
if original_img is None:
    print("이미지를 찾을 수 없습니다. 경로를 확인해 주세요.")
    exit()

# 2. 윈도우 생성
window_name = 'Image Processing'
cv2.namedWindow(window_name)

# 3. 트랙바 생성
# cv2.createTrackbar(트랙바 이름, 윈도우 이름, 초기값, 최대값, 콜백 함수)
# 밝기: -100 ~ 100을 표현하기 위해 0~200으로 설정하고 기준점을 100으로 잡음
cv2.createTrackbar('Brightness', window_name, 100, 200, nothing) 
# 대비: 0.0 ~ 3.0을 표현하기 위해 0~300으로 설정하고 기준점을 100으로 잡음
cv2.createTrackbar('Contrast', window_name, 100, 300, nothing) 
# 캐니 에지 임계값 (0 ~ 255)
cv2.createTrackbar('Canny Low', window_name, 50, 255, nothing)
cv2.createTrackbar('Canny High', window_name, 150, 255, nothing)
# 모드 전환 (0: 흑백, 1: 캐니 에지)
cv2.createTrackbar('Mode (0:Gray, 1:Edge)', window_name, 0, 1, nothing)

while True:
    # 4. 트랙바의 현재 값 가져오기
    b_val = cv2.getTrackbarPos('Brightness', window_name) - 100 # -100 ~ 100
    c_val = cv2.getTrackbarPos('Contrast', window_name) / 100.0 # 0.0 ~ 3.0
    low_thresh = cv2.getTrackbarPos('Canny Low', window_name)
    high_thresh = cv2.getTrackbarPos('Canny High', window_name)
    mode = cv2.getTrackbarPos('Mode (0:Gray, 1:Edge)', window_name)

    # 5. 밝기 및 대비 조절
    # 수식: 결과 = 원본 * 대비 + 밝기
    # cv2.convertScaleAbs는 계산 결과가 0~255 범위를 벗어나지 않도록 안전하게 처리합니다.
    adjusted_img = cv2.convertScaleAbs(original_img, alpha=c_val, beta=b_val)

    # 6. 흑백(Grayscale) 변환
    gray_img = cv2.cvtColor(adjusted_img, cv2.COLOR_BGR2GRAY)

    # 7. 모드에 따라 출력 이미지 결정
    if mode == 1:
        # 캐니 에지 적용
        result_img = cv2.Canny(gray_img, low_thresh, high_thresh)
    else:
        # 흑백 이미지 출력
        result_img = gray_img

    # 화면에 출력
    cv2.imshow(window_name, result_img)

    # ESC 키(27)를 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 모든 윈도우 닫기
cv2.destroyAllWindows()