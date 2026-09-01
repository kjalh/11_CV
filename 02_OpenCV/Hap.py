import cv2
import numpy as np
import sys

# 글로벌 변수 선언 (콜백 함수에서 접근하기 위함)
src_color = None
src_gray = None

# 1. 이진화(Threshold) 트랙바 콜백 함수
def on_threshold_trackbar(val):
    _, dst = cv2.threshold(src_gray, val, 255, cv2.THRESH_BINARY)
    cv2.imshow("Binary Image", dst)

# 2. 가우시안 블러(Gaussian Blur) 트랙바 콜백 함수
def on_blur_trackbar(val):
    ksize = val
    if ksize < 1:
        ksize = 1
    elif ksize % 2 == 0:
        ksize += 1
        
    dst = cv2.GaussianBlur(src_color, (ksize, ksize), 0)
    cv2.imshow("Gaussian Blur", dst)

# 3. 샤프닝(Sharpening) 트랙바 콜백 함수
def on_trackbar_sharpen(val):
    alpha = val
    kernel = np.array([[ 0,      -alpha,      0],
                       [-alpha, 1 + 4*alpha, -alpha],
                       [ 0,      -alpha,      0]], dtype=np.float32)
    
    dst = cv2.filter2D(src_color, -1, kernel)
    cv2.imshow("Sharpening Image", dst)

# 메인 실행부
if __name__ == "__main__":
    # 이미지 경로 설정
    image_path = "./images/park.png"
    
    # 컬러 및 흑백 이미지 읽기
    src_color = cv2.imread(image_path)
    src_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if src_color is None or src_gray is None:
        print("이미지를 찾을 수 없습니다. 경로를 확인해 주세요.")
        sys.exit()

    # 원본 이미지 출력 (비교용)
    cv2.imshow("Original Image (Color)", src_color)
    
    # 트랙바를 붙일 창 미리 생성
    cv2.namedWindow("Binary Image")
    cv2.namedWindow("Gaussian Blur")
    cv2.namedWindow("Sharpening Image")

    # 트랙바 생성 (이름, 창 이름, 초기값, 최대값, 콜백 함수)
    cv2.createTrackbar("Threshold", "Binary Image", 128, 255, on_threshold_trackbar)
    cv2.createTrackbar("Kernel Size", "Gaussian Blur", 1, 60, on_blur_trackbar)
    cv2.createTrackbar("Strength", "Sharpening Image", 1, 10, on_trackbar_sharpen)

    # 프로그램 실행 시 초기 화면을 보여주기 위해 강제 호출
    on_threshold_trackbar(128)
    on_blur_trackbar(1)
    on_trackbar_sharpen(1)

    # 키 입력 대기 (아무 키나 누르면 종료) 및 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()