import cv2
from picamera2 import Picamera2
import numpy as np
from ultralytics import YOLO

# 카메라 초기화
picam2 = Picamera2()
picam2.preview_configuration.main.size = (1024, 720)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# YOLO 모델 로드
model = YOLO("bestsegn.pt")
yolo_classes = list(model.names.values())

# CLAHE 객체 생성
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

# 클래스별 색상 지정 (2개 이상 클래스인 경우 대비되게 설정 필요)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

count = 0
fps = 0
prev_time = 0

while True:
    frame = picam2.capture_array()
    frame = cv2.flip(frame, -1)

    # CLAHE 적용 (LAB 색공간 L채널만 조정)
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    cl = clahe.apply(l)
    limg = cv2.merge((cl, a, b))
    clahe_frame = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    # YOLO는 clahe_frame 기준으로 탐지
    count += 1
    if count % 3 != 0:
        current_time = cv2.getTickCount() / cv2.getTickFrequency()
        fps = 1 / (current_time - prev_time)
        prev_time = current_time
        continue

    results = model.predict(clahe_frame, imgsz=640)
    overlay = clahe_frame.copy()

    for result in results:
        if result.masks is not None and result.boxes is not None:
            for mask, box in zip(result.masks.xy, result.boxes):
                points = np.int32([mask])
                class_id = int(box.cls[0])
                class_name = yolo_classes[class_id]

                color = colors[class_id % len(colors)]
                cv2.polylines(overlay, [points], True, color, 1)
                cv2.fillPoly(overlay, [points], color)

                # 바운딩 박스와 텍스트 표시
                x, y, w, h = box.xyxy[0].numpy()
                x1, y1, x2, y2 = map(int, [x, y, w, h])
                text_position = (int((x1 + x2) / 2), int(y1 - 10))
                cv2.putText(overlay, f"{class_name}", text_position,
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2, cv2.LINE_AA)

    # 투명도 적용
    alpha = 0.7
    cv2.addWeighted(overlay, alpha, clahe_frame, 1 - alpha, 0, clahe_frame)

    # FPS 표시
    current_time = cv2.getTickCount() / cv2.getTickFrequency()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    cv2.putText(clahe_frame, f"FPS: {fps:.2f}", (10, 32), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # 결과 출력
    cv2.imshow("CLAHE + YOLO", clahe_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 종료 처리
picam2.stop()
cv2.destroyAllWindows()
