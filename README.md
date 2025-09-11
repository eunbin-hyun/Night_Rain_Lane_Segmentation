# Night & Rain Lane_Segmentation
야간 및 악천후 시 차선감지 AI 시스템

![기존한계](https://github.com/user-attachments/assets/afbeddcf-9f4a-4b7b-aa4e-e9979ec06bbe) | ![아이디어](https://github.com/user-attachments/assets/455fb96a-5079-43e5-87d7-5b11186ee26c)
---|---|

## ⚙️ Tech Stack

| 🚀**Hardware** | 💻**Software** |
|--------------|--------------|
| **Raspberry Pi 5** – 실시간 영상 처리 및 AI 모델 추론 | **OpenCV** – 이미지 전처리(CLAHE), 밝기조절 |
| **Picamera v3** – YOLO Segmentation 입력 영상 수집 | **YOLOv11 Segmentation** – 실시간 차선·객체 인식 |
| **Polarizing Film** – 야간·우천 시 반사광 억제 |


## 🏁 Result

![실험결과](https://github.com/user-attachments/assets/4081d63d-472c-45de-b7b9-aaa58de9d0db) | ![테스트결과](https://github.com/user-attachments/assets/6cd59bf0-0dfb-47d3-9dc9-9e2668c0296a)
---|---|
|📊 **성능 비교 **|🧪 **실험 결과** |
|- 개선 버전: OpenCV 전처리 + 편광필름 적용 | - 야간·우천 환경 모두에서 **yellow_line, white_line을 안정적으로 검출**|
|- 기존 모델 대비 재현율(Recall) **28.7% ↑**, mAP50 **11.2% ↑** | - 실시간 테스트에서 FPS 1.54 달성|
