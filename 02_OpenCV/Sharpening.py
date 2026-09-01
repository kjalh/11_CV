import cv2
import numpy as np
import sys

# 트랙바 콜백 함수
def on_trackbar(val):
    # val 값(강도)을 alpha로 사용 (0이면 원본, 커질수록 샤프닝 강해짐)
    alpha = val
    
    # 동적 샤프닝 커널 생성
    # 상하좌우는 -alpha, 중앙은 (1 + 4 * alpha)로 설정하여 항상 전체 합이 1이 되도록 맞춤
    # 예: val=1일 때 -> 중앙 5, 상하좌우 -1 (기존과 동일)
    # 예: val=2일 때 -> 중앙 9, 상하좌우 -2 (더 강한 샤프닝)
    kernel = np.array([[ 0,      -alpha,      0],
                       [-alpha, 1 + 4*alpha, -alpha],
                       [ 0,      -alpha,      0]], dtype=np.float32)
    
    # 필터 적용
    dst = cv2.filter2D(src, -1, kernel)
    
    # 결과 출력
    cv2.imshow("Sharpening Image", dst)

# 메인 실행부
if __name__ == "__main__":
    # 이미지 읽기 (실제 이미지 경로로 변경해 주세요)
    src = cv2.imread("./images/park.png")

    if src is None:
        print("Could not open or find the image!")
        sys.exit()

    # 원본 이미지 출력
    cv2.imshow("Original Image", src)

    # 트랙바를 붙일 창 미리 생성
    cv2.namedWindow("Sharpening Image")

    # 트랙바 생성
    # 파라미터: 트랙바 이름, 창 이름, 초기값(1), 최대값(10), 콜백 함수
    # 강도가 너무 커지면 이미지가 깨지므로 최대값을 10 정도로 제한하는 것이 좋습니다.
    cv2.createTrackbar("Strength", "Sharpening Image", 1, 10, on_trackbar)

    # 초기 화면 출력을 위해 강제 호출 (강도 1 적용)
    on_trackbar(1)

    # 키 입력 대기 및 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()