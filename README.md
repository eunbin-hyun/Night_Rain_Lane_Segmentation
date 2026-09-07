# 🌧️ Night & Rain Lane Segmentation

> 편광필름과 CLAHE 전처리, YOLO11 Segmentation을 결합한 야간·우천 차선 인식 시스템

`YOLO11n-seg` · `OpenCV` · `CLAHE` · `Raspberry Pi 5` · `Picamera2`

## 문제 정의

야간과 우천 환경에서는 노면 반사광, 낮은 대비, 빗물로 인한 번짐 때문에 차선의 경계가 흐려집니다. 일반 주행 영상으로 학습한 모델은 이 조건에서 흰색·노란색 차선을 놓치기 쉬워, 광학적 노이즈 억제와 영상 대비 개선을 함께 적용했습니다.

| 기존 한계 | 해결 아이디어 |
|---|---|
| ![야간 우천 환경의 기존 한계](https://github.com/user-attachments/assets/afbeddcf-9f4a-4b7b-aa4e-e9979ec06bbe) | ![편광필름과 AI를 결합한 해결 아이디어](https://github.com/user-attachments/assets/455fb96a-5079-43e5-87d7-5b11186ee26c) |

## 해결 방법

```text
Picamera2 입력
  → 편광필름으로 노면 반사 억제
  → LAB 색공간의 L 채널에 CLAHE 적용
  → YOLO11n-seg로 white_line / yellow_line 분할
  → 마스크 overlay와 FPS 표시
```

### 1. 광학·영상 전처리

- 카메라 전면에 편광필름을 적용해 젖은 노면의 반사광을 완화
- RGB 영상을 LAB 색공간으로 변환
- 밝기 정보인 L 채널에 `clipLimit=2.0`, `tileGridSize=(8, 8)` CLAHE 적용
- 색 정보는 유지하면서 저조도 영역의 국부 대비를 강화

### 2. 차선 인스턴스 분할

- YOLO11n Segmentation으로 `yellow_line`, `white_line` 클래스 학습
- bounding box보다 차선 형상을 잘 보존하도록 polygon mask 사용
- Raspberry Pi 5에서 입력 영상을 640px로 추론
- 처리 부하를 조절하기 위해 3프레임마다 추론하고, 결과 마스크와 FPS를 실시간 표시

### 3. 임베디드 추론

- Picamera2에서 1024×720 RGB 영상을 수집
- OpenCV로 CLAHE 전처리와 mask overlay 수행
- Raspberry Pi 5에서 카메라 입력부터 시각화까지 하나의 파이프라인으로 통합
- 구현 코드: [`main_clahe.py`](./main_clahe.py)

## 구현 결과

| 성능 비교 | 야간·우천 테스트 |
|---|---|
| ![기존 모델과 개선 모델의 성능 비교](https://github.com/user-attachments/assets/45b5baf6-c1b4-47af-8f1f-879dd02035cf) | ![야간 및 우천 차선 분할 테스트](https://github.com/user-attachments/assets/8c406475-1547-45e0-9e92-2bac298b65ad) |

- 기존 모델 대비 **Recall 28.7%p 향상**
- 기존 모델 대비 **mAP50 11.2%p 향상**
- 야간·우천 환경에서 노란색·흰색 차선을 segmentation mask로 구분

> 위 수치는 프로젝트 실험 조건의 기존 모델과 개선 모델을 비교한 결과입니다. 다른 데이터셋이나 카메라 환경에 그대로 일반화되는 수치는 아닙니다.

## 담당 역할

- 팀장으로 문제 정의, 실험 계획, 일정과 발표를 총괄
- 야간·우천 차선 데이터 수집과 segmentation 라벨링
- YOLO11n-seg 모델 학습과 성능 비교
- 편광필름·CLAHE 조합의 전처리 실험
- Raspberry Pi 5·Picamera2 실시간 추론 코드 구현

## 저장소 구조

```text
Night_Rain_Lane_Segmentation/
├─ castone2_yolov11n_seg.ipynb   # YOLO11 segmentation 학습·검증
├─ main_clahe.py                  # 카메라·CLAHE·실시간 추론
├─ best.pt                        # 학습 모델 weight
└─ docs/                          # 학술대회 논문
```

## 성과와 발표

- 2025 한국전기전자학회 하계학술대회 제1저자
  - **야간 및 악천후 환경에서의 딥러닝 기반 실시간 차선 인식 시스템**
  - [논문 PDF](./docs/2025%20하계학술대회%20논문%20-%20야간%20및%20악천후%20환경에서의%20딥러닝%20기반%20실시간%20차선%20인식%20시스템.pdf)
- 2025-1학기 캡스톤디자인 결과발표회 **우수상**
