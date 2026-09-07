# 🌧️ Night & Rain Lane Segmentation

> 편광필름과 CLAHE 전처리, 딥러닝 세그멘테이션을 결합한 야간·우천 차선 인식 시스템

`YOLO11n-seg` · `BiSeNetV2` · `OpenCV` · `CLAHE` · `TensorRT` · `Raspberry Pi 5` · `Jetson Orin Nano`

## 프로젝트 개요

야간과 우천 환경에서는 낮은 조도, 젖은 노면의 반사광, 빗물 번짐으로 차선 경계가 흐려집니다. 이 프로젝트는 광학적 반사 억제와 영상 대비 개선, 딥러닝 세그멘테이션을 결합해 악천후 환경에서도 차선을 안정적으로 인식하는 것을 목표로 합니다.

캡스톤디자인 **「AI기반 악천후 감지 시스템」**으로 시작했으며, Raspberry Pi 5 기반 실시간 구현과 Jetson Orin Nano 기반 모델 비교 연구로 확장했습니다.

## 문제 정의

| 문제 | 영향 | 적용 방법 |
|---|---|---|
| 젖은 노면의 강한 반사광 | 차선과 배경의 경계가 흐려짐 | 카메라 전면에 편광필름 적용 |
| 야간 영상의 낮은 대비 | 흰색·노란색 차선 누락 | LAB 색공간의 L 채널에 CLAHE 적용 |
| 임베디드 환경의 제한된 연산 성능 | 추론 속도 저하 | 경량 모델 비교 및 TensorRT FP16 최적화 |

| 기존 한계 | 해결 아이디어 |
|---|---|
| ![야간 우천 환경의 기존 한계](https://github.com/user-attachments/assets/afbeddcf-9f4a-4b7b-aa4e-e9979ec06bbe) | ![편광필름과 AI를 결합한 해결 아이디어](https://github.com/user-attachments/assets/455fb96a-5079-43e5-87d7-5b11186ee26c) |

## 구현 방법

### 1. 광학·영상 전처리

- 카메라 전면에 편광필름을 적용해 젖은 노면의 반사광 완화
- RGB 영상을 LAB 색공간으로 변환
- 밝기 정보인 L 채널에 `clipLimit=2.0`, `tileGridSize=(8, 8)` CLAHE 적용
- 색 정보는 유지하면서 저조도 영역의 국부 대비 강화

### 2. 데이터셋과 모델 학습

- AI-Hub 데이터 1,461장과 직접 촬영한 야간·우천 데이터 400장 활용
- `yellow_line`, `white_line` 클래스를 polygon mask로 라벨링
- YOLOv5n-seg, YOLOv8n-seg, YOLO11n-seg 학습 및 성능 비교
- Jetson Orin Nano 연구에서 YOLO11n-seg와 경량 시맨틱 세그멘테이션 모델 BiSeNetV2 비교

### 3. 임베디드 실시간 추론

- Raspberry Pi 5와 Picamera2를 이용해 카메라 입력부터 전처리·추론·시각화까지 통합
- 640px 입력과 프레임 간격 추론을 적용해 제한된 연산 환경의 부하 조절
- Jetson Orin Nano에서 TensorRT FP32·FP16 엔진의 정확도와 처리 속도 측정
- 구현 코드: [`main_clahe.py`](./main_clahe.py)

## 구현 결과

| 성능 비교 | 야간·우천 테스트 |
|---|---|
| ![기존 모델과 개선 모델의 성능 비교](https://github.com/user-attachments/assets/45b5baf6-c1b4-47af-8f1f-879dd02035cf) | ![야간 및 우천 차선 분할 테스트](https://github.com/user-attachments/assets/8c406475-1547-45e0-9e92-2bac298b65ad) |

### Raspberry Pi 5

- YOLO11n-seg 기준 **mAP50 0.856**, 실시간 추론 **1.54 FPS**
- 기존 모델 대비 **Recall 28.7%p**, **mAP50 11.2%p 향상**
- 야간·우천 환경에서 노란색·흰색 차선을 segmentation mask로 구분

### Jetson Orin Nano

| 모델 | CLAHE 적용 mIoU | FP32 | FP16 |
|---|---:|---:|---:|
| YOLO11n-seg | 0.8572 | 8.54 FPS | 10.07 FPS |
| BiSeNetV2 | **0.8691** | **10.94 FPS** | **12.58 FPS** |

- 정확도와 추론 속도를 종합해 **CLAHE + BiSeNetV2** 조합의 활용 가능성 확인
- 전처리 적용 BiSeNetV2에서 Precision **0.972**, Recall **0.874** 기록

> 성능 수치는 각 논문의 데이터셋과 실험 환경을 기준으로 하며, 다른 카메라나 데이터 환경에서는 달라질 수 있습니다.

## 담당 역할

- 팀장으로 문제 정의, 실험 계획, 일정 관리 및 발표 총괄
- 야간·우천 차선 데이터 직접 수집 및 세그멘테이션 라벨링
- YOLO 계열 모델과 BiSeNetV2 학습·평가
- 편광필름과 CLAHE 조합의 전처리 실험
- Raspberry Pi 5 및 Jetson Orin Nano 추론 환경 구축
- 두 학술대회 논문 **제1저자**, 논문 작성 및 현장 발표

## 성과와 발표

- **2025-1학기 캡스톤디자인 결과발표회 우수상**
  - 프로젝트: 「AI기반 악천후 감지 시스템」
  - [발표자료](./docs/capstone/presentation.pdf)
- **2025 한국전기전자학회 하계학술대회 제1저자·발표자**
  - 논문: 「야간 및 악천후 환경에서의 딥러닝 기반 실시간 차선 인식 시스템」
  - [논문](./docs/raspberry-pi/paper.pdf) · [포스터](./docs/raspberry-pi/poster.pdf)
- **제27회 전자정보통신 학술대회 제1저자·발표자**
  - 논문: 「야간 및 악천후 환경에서의 차선 인식용 세그멘테이션 모델 비교」
  - [논문](./docs/jetson-orin-nano/paper.pdf) · [발표자료](./docs/jetson-orin-nano/presentation.pdf)

## 저장소 구조

```text
Night_Rain_Lane_Segmentation/
├─ castone2_yolov11n_seg.ipynb       # YOLO11 segmentation 학습·검증
├─ main_clahe.py                      # 카메라·CLAHE·실시간 추론
├─ best.pt                            # 학습 모델 weight
└─ docs/
   ├─ README.md                       # 연구 이력과 문서 안내
   ├─ capstone/                       # 캡스톤디자인 발표자료
   ├─ raspberry-pi/                   # 하계학술대회 논문·포스터
   └─ jetson-orin-nano/               # 전자정보통신 학술대회 논문·발표자료
```

연구 확장 과정과 전체 문서는 [`docs/README.md`](./docs/README.md)에서 확인할 수 있습니다.
