# 🌧️ Night & Rain Lane Segmentation

> 캡스톤디자인에서 시작해 Raspberry Pi 5와 Jetson Orin Nano로 확장한 야간·악천후 실시간 차선 인식 연구

`YOLO11n-seg` · `BiSeNetV2` · `OpenCV` · `CLAHE` · `TensorRT` · `Raspberry Pi 5` · `Jetson Orin Nano`

## 프로젝트 개요

야간과 우천 환경에서는 낮은 조도, 젖은 노면의 반사광, 빗물 번짐으로 차선 경계가 흐려집니다. 이 프로젝트는 **편광필름을 이용한 광학적 반사 억제**, **CLAHE 기반 대비 개선**, **딥러닝 세그멘테이션**을 결합해 악천후 환경에서도 차선을 실시간으로 인식하는 것을 목표로 합니다.

캡스톤디자인 **「AI기반 악천후 감지 시스템」**으로 구현한 뒤, Raspberry Pi 5 기반 실시간 시스템과 Jetson Orin Nano 기반 모델 비교 연구로 발전시켰습니다.

| 단계 | 플랫폼 | 주요 내용 | 성과 |
|---|---|---|---|
| 캡스톤디자인 | Raspberry Pi 기반 프로토타입 | 편광필름·CLAHE·차선 세그멘테이션 결합 | 2025-1학기 캡스톤디자인 결과발표회 **우수상** |
| 1차 연구 | Raspberry Pi 5 | YOLO 계열 모델 비교 및 실시간 추론 시스템 구현 | 한국전기전자학회 하계학술대회 **제1저자·발표자** |
| 2차 연구 | Jetson Orin Nano | YOLO11n-seg와 BiSeNetV2 비교, TensorRT FP16 최적화 | 제27회 전자정보통신 학술대회 **제1저자·발표자** |

## 연구 흐름

```text
카메라 입력
  → 편광필름으로 젖은 노면의 반사광 억제
  → LAB 색공간의 L 채널에 CLAHE 적용
  → 딥러닝 모델로 white_line / yellow_line 분할
  → 임베디드 보드에서 실시간 추론 및 결과 시각화
```

### 1. 캡스톤디자인 — AI기반 악천후 감지 시스템

- 야간·우천 환경에서 발생하는 반사광과 낮은 대비 문제 정의
- 편광필름과 CLAHE 전처리를 결합한 차선 인식 파이프라인 설계
- 데이터 수집·라벨링, 모델 학습, 임베디드 추론, 발표까지 통합 수행
- 2025-1학기 캡스톤디자인 결과발표회 **우수상** 수상
- [캡스톤 발표자료](./docs/capstone/presentation.pdf)

### 2. Raspberry Pi 5 — 실시간 차선 인식 시스템

**논문:** 「야간 및 악천후 환경에서의 딥러닝 기반 실시간 차선 인식 시스템」

- AI-Hub 데이터 1,461장과 직접 촬영한 야간·우천 데이터 400장 활용
- YOLOv5n-seg, YOLOv8n-seg, YOLO11n-seg 성능 비교
- Raspberry Pi 5와 Picamera2를 이용한 실시간 추론 파이프라인 구현
- YOLO11n-seg 기준 `mAP50 0.856`, Raspberry Pi 5에서 `1.54 FPS` 기록
- 기존 모델 대비 **Recall 28.7%p**, **mAP50 11.2%p 향상**
- **제1저자 및 논문 발표 담당**
- [논문 PDF](./docs/raspberry-pi/paper.pdf) · [학술대회 포스터](./docs/raspberry-pi/poster.pdf)

### 3. Jetson Orin Nano — 세그멘테이션 모델 비교

**논문:** 「야간 및 악천후 환경에서의 차선 인식용 세그멘테이션 모델 비교」

- Raspberry Pi 기반 연구를 Jetson Orin Nano 환경으로 확장
- YOLO11n-seg와 경량 시맨틱 세그멘테이션 모델 BiSeNetV2 비교
- TensorRT 변환 후 FP32·FP16 추론 성능 측정
- CLAHE 전처리 적용 시 `mIoU`: YOLO11n-seg **0.8572**, BiSeNetV2 **0.8691**
- FP16 추론 속도: YOLO11n-seg **10.07 FPS**, BiSeNetV2 **12.58 FPS**
- 정확도와 처리 속도를 종합해 **CLAHE + BiSeNetV2** 조합의 활용 가능성 확인
- **제1저자 및 논문 발표 담당**
- [논문 PDF](./docs/jetson-orin-nano/paper.pdf) · [발표자료](./docs/jetson-orin-nano/presentation.pdf)

## 구현 방법

### 광학·영상 전처리

- 카메라 전면의 편광필름으로 젖은 노면의 반사광 완화
- RGB 영상을 LAB 색공간으로 변환
- 밝기 정보인 L 채널에 `clipLimit=2.0`, `tileGridSize=(8, 8)` CLAHE 적용
- 색 정보는 유지하면서 저조도 영역의 국부 대비 강화

### 딥러닝 세그멘테이션

- `yellow_line`, `white_line` 클래스를 polygon mask로 라벨링
- Raspberry Pi 단계에서는 YOLO11n-seg 기반 인스턴스 세그멘테이션 적용
- Jetson Orin Nano 단계에서는 YOLO11n-seg와 BiSeNetV2를 동일 환경에서 비교
- TensorRT FP16 최적화로 임베디드 추론 속도 향상

## 구현 결과

| 성능 비교 | 야간·우천 테스트 |
|---|---|
| ![기존 모델과 개선 모델의 성능 비교](https://github.com/user-attachments/assets/45b5baf6-c1b4-47af-8f1f-879dd02035cf) | ![야간 및 우천 차선 분할 테스트](https://github.com/user-attachments/assets/8c406475-1547-45e0-9e92-2bac298b65ad) |

> 성능 수치는 각 논문에 기재된 실험 환경과 데이터셋을 기준으로 하며, 다른 카메라나 데이터 환경에서는 달라질 수 있습니다.

## 담당 역할

- 팀장으로 문제 정의, 실험 계획, 일정 관리 및 발표 총괄
- 야간·우천 차선 데이터 직접 수집 및 세그멘테이션 라벨링
- YOLO 계열 모델과 BiSeNetV2 학습·평가
- 편광필름과 CLAHE 조합의 전처리 실험
- Raspberry Pi 5 및 Jetson Orin Nano 추론 환경 구축
- 두 학술대회 논문 **제1저자**, 논문 작성 및 현장 발표

## 저장소 구조

```text
Night_Rain_Lane_Segmentation/
├─ castone2_yolov11n_seg.ipynb       # YOLO11 segmentation 학습·검증
├─ main_clahe.py                      # 카메라·CLAHE·실시간 추론
├─ best.pt                            # 학습 모델 weight
└─ docs/
   ├─ README.md                       # 논문·발표자료 안내
   ├─ capstone/                       # 캡스톤디자인 발표자료
   ├─ raspberry-pi/                   # 하계학술대회 논문·포스터
   └─ jetson-orin-nano/               # 전자정보통신 학술대회 논문·발표자료
```

## 문서 모음

논문과 발표자료는 [`docs/README.md`](./docs/README.md)에서 한 번에 확인할 수 있습니다.