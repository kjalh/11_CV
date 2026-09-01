import cv2
import numpy as np

img = cv2.imread("./images/namecard.jpg")

# 변환된 크기를 이렇게 할거다
dst_w = 600
dst_h = 400

# 네 점의 순서는 왼쪽 위 > 오른쪽 위 > 오른쪽 아래 > 왼쪽 아래
src_quad = np.array([
    [16, 16],    
    [700, 16],   
    [700, 843],  
    [16, 843]     
], dtype=np.float32)

dst_quad = np.array([
    [0, 0],
    [dst_w - 1, 0],
    [dst_w - 1, dst_h - 1],
    [0, dst_h - 1]
], dtype=np.float32)

perspective_matrix = cv2.getPerspectiveTransform(src_quad, dst_quad)
print(perspective_matrix)

dst = cv2.warpPerspective(img, perspective_matrix, (dst_w, dst_h))

preview = img.copy()
for pt in src_quad.astype(int):
    cv2.circle(preview, tuple(pt), 8, (0, 0, 255), -1)

cv2.polylines(preview, [src_quad.astype(np.int32)], True, (0, 255, 0), 3)

cv2.imshow("preview", preview)
cv2.imshow("perspective result", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()