# Night & Rain Lane_Segmentation
**야간 및 악천후 시 차선감지 AI 시스템**

<br>

## 문제 정의 & 해결 아이디어
![기존한계](https://github.com/user-attachments/assets/afbeddcf-9f4a-4b7b-aa4e-e9979ec06bbe) | ![아이디어](https://github.com/user-attachments/assets/455fb96a-5079-43e5-87d7-5b11186ee26c)
---|---|

<br>

## ⚙️ Tech Stack
### 🚀 Hardware
- **Raspberry Pi 5** – 실시간 영상 처리 및 AI 모델 추론
- **Picamera v3** – YOLO Segmentation 입력 영상 수집
- **Polarizing Film** – 야간·우천 시 반사광 억제

### 💻 Software
- **OpenCV** – 이미지 전처리(CLAHE), 영상 처리
- **YOLOv8 Segmentation** – 실시간 차선·객체 인식

<br>

## 🏁 Result

![실험결과](https://github.com/user-attachments/assets/45b5baf6-c1b4-47af-8f1f-879dd02035cf) | ![테스트결과](https://github.com/user-attachments/assets/8c406475-1547-45e0-9e92-2bac298b65ad)
---|---|
|📊 **성능 비교**|🧪 **실험 결과** |
| 개선 버전: OpenCV 전처리 + 편광필름 적용 | 야간·우천 환경 모두에서 **yellow_line, white_line을 안정적으로 검출**|
| 기존 모델 대비 재현율(Recall) **28.7% ↑**, mAP50 **11.2% ↑** | 
