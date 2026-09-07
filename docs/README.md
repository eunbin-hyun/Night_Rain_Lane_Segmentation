# 연구 이력 및 문서

**「AI기반 악천후 감지 시스템」**에서 시작해 Raspberry Pi 5와 Jetson Orin Nano로 확장한 연구 결과를 정리합니다.

## 연구 확장 과정

| 구분 | 플랫폼 | 연구 내용 | 결과 |
|---|---|---|---|
| 캡스톤디자인 | Raspberry Pi 기반 프로토타입 | 편광필름·CLAHE·차선 세그멘테이션 결합 | 2025-1학기 캡스톤디자인 결과발표회 **우수상** |
| 1차 연구 | Raspberry Pi 5 | YOLO 계열 비교 및 실시간 차선 인식 시스템 구현 | 학술대회 논문 발표 |
| 2차 연구 | Jetson Orin Nano | YOLO11n-seg·BiSeNetV2 비교 및 TensorRT 최적화 | 학술대회 논문 발표 |

## 1. 캡스톤디자인

- 프로젝트명: **AI기반 악천후 감지 시스템**
- 성과: **2025-1학기 캡스톤디자인 결과발표회 우수상**
- 자료: [발표자료](./capstone/presentation.pdf)

## 2. Raspberry Pi 5 기반 연구

- 논문명: **야간 및 악천후 환경에서의 딥러닝 기반 실시간 차선 인식 시스템**
- 학술대회: **2025 한국전기전자학회 하계학술대회**
- 역할: **제1저자·발표자**
- 자료: [논문](./raspberry-pi/paper.pdf) · [포스터](./raspberry-pi/poster.pdf)

## 3. Jetson Orin Nano 기반 연구

- 논문명: **야간 및 악천후 환경에서의 차선 인식용 세그멘테이션 모델 비교**
- 학술대회: **제27회 전자정보통신 학술대회**
- 역할: **제1저자·발표자**
- 자료: [논문](./jetson-orin-nano/paper.pdf) · [발표자료](./jetson-orin-nano/presentation.pdf)

## 파일명 구성

각 단계가 폴더명으로 구분되므로 파일명은 문서 종류만 표시했습니다.

```text
docs/
├─ capstone/
│  └─ presentation.pdf
├─ raspberry-pi/
│  ├─ paper.pdf
│  └─ poster.pdf
└─ jetson-orin-nano/
   ├─ paper.pdf
   └─ presentation.pdf
```
