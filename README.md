# 🛡️ Women Safety Analytics

A Python-based analytics system that processes live video/sensor streams using Machine Learning to detect potentially unsafe situations in public spaces — such as unusual crowd gender ratios, distress gestures, or lone-woman-at-night patterns — and raises real-time alerts.

## 📌 Overview

Public safety monitoring today relies heavily on manual CCTV watching, which doesn't scale. This project applies **computer vision and machine learning** to video streams (e.g. from CCTV/IP cameras) to flag scenarios that may indicate risk to women's safety — like a lone woman surrounded by a group of men at night, sudden distress gestures, or abnormal loitering patterns — and sends real-time alerts to control room dashboards or security personnel.

> ⚠️ **Note:** This is intended as an assistive analytics/decision-support tool for authorities, not a replacement for human judgment or law enforcement. Care must be taken around bias, privacy, and false positives before any real-world deployment.

## ✨ Features

- 🎥 Real-time video stream processing (RTSP/webcam/CCTV feed)
- 🧍‍♀️ Person detection & gender classification (aggregate, not individual profiling)
- 🚨 Lone-woman-at-night detection
- 👥 Abnormal gender-ratio / surrounding pattern detection
- 🙋 Distress gesture recognition (SOS hand signal, sudden running)
- 📊 Analytics dashboard with incident logs & heatmaps
- 🔔 Real-time alerting (console/webhook/SMS-ready)

## 🛠️ Tech Stack

- **Python 3.9+**
- **OpenCV** — video stream capture & preprocessing
- **YOLOv8 (Ultralytics)** — person detection
- **Machine Learning classifier** — gender classification model (trained/fine-tuned separately)
- **MediaPipe** — pose/gesture estimation for distress signals
- **Flask** — lightweight alert/dashboard backend
- **SQLite/CSV** — incident logging

## 📂 Project Structure

```
women-safety-analytics/
├── src/
│   ├── stream_processor.py     # Captures & processes video stream frame-by-frame
│   ├── detection.py            # Person detection + gender classification logic
│   ├── gesture_analysis.py     # Distress gesture / pose-based analysis
│   ├── alert_manager.py        # Handles alert triggering & logging
│   └── main.py                 # Entry point - orchestrates the pipeline
├── models/
│   └── README.md                # Notes on model weights (not included, see below)
├── docs/
│   └── ethical_considerations.md
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 1. Set up environment
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Add model weights
Download a pretrained YOLOv8 model (e.g. `yolov8n.pt` from Ultralytics) and place it in `models/`. Gender classification and gesture models should be trained/fine-tuned on appropriate, consented, and bias-audited datasets — see `docs/ethical_considerations.md`.

### 3. Run the pipeline
```bash
python src/main.py --source 0        # webcam
python src/main.py --source rtsp://your-camera-stream-url
```

## ⚙️ How It Works

1. `stream_processor.py` pulls frames from the video source (webcam, RTSP CCTV feed, or video file).
2. `detection.py` runs person detection (YOLOv8) and aggregate gender classification per frame.
3. `gesture_analysis.py` uses MediaPipe pose landmarks to flag distress gestures or sudden erratic movement.
4. Contextual rules (time of day + lone individual + surrounding count) combine these signals to compute a risk score.
5. `alert_manager.py` logs incidents and triggers alerts (console output by default; extendable to SMS/webhook/control-room dashboard).

## 📈 Future Improvements

- Integration with municipal CCTV control rooms via RTSP aggregation
- Heatmap-based "unsafe zone" analytics over time
- Mobile panic-button app integration
- On-device edge inference (Jetson Nano/Coral) for privacy-preserving deployment

## ⚖️ Ethical & Privacy Considerations

See [`docs/ethical_considerations.md`](docs/ethical_considerations.md) — this system involves human subject detection and must be deployed with strict attention to privacy law, consent, bias auditing, and oversight to avoid misuse or false positives.

## 📄 License

MIT License — feel free to use and modify.
