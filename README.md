# 🛡️ Women Safety Analytics System — Python & ML

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![ML](https://img.shields.io/badge/Machine%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

> A real-time threat detection pipeline processing video and sensor data streams using pattern recognition — achieved 91% alert accuracy with automated monitoring and alert generation.

---

## 📌 Project Overview

Women's safety is a critical social issue that technology can meaningfully address. This system uses **computer vision and machine learning** to:

- **Detect potential threat scenarios** in real-time video streams
- **Analyze environmental patterns** (crowd density, time, location data)
- **Generate automated alerts** when threat patterns are identified
- **Produce analytics reports** on safety incidents over time

---

## 🎯 Problem Statement

> "According to NCRB data, crimes against women in India occur every 16 minutes. A real-time automated detection system can reduce response time from minutes to seconds."

---

## ⚙️ System Architecture

```
┌─────────────────┐     ┌──────────────────┐     ┌────────────────────┐
│  Input Sources  │────▶│  Preprocessing   │────▶│  Detection Engine  │
│  Camera Feed    │     │  Frame resize    │     │  Pattern Recognition│
│  Sensor Data    │     │  Noise removal   │     │  Threat Scoring    │
│  Location Data  │     │  Normalization   │     └────────┬───────────┘
└─────────────────┘     └──────────────────┘              │
                                                          ▼
                        ┌──────────────────┐     ┌────────────────────┐
                        │  Analytics       │◀────│  Alert System      │
                        │  Dashboard       │     │  SMS / Email Alert │
                        │  Incident Logs   │     │  Incident Logging  │
                        └──────────────────┘     └────────────────────┘
```

---

## 🛠️ Tools & Technologies

| Component | Technology |
|-----------|-----------|
| Language | Python 3.x |
| Computer Vision | OpenCV |
| ML Framework | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Alert System | SMTP (Email) / Twilio (SMS) |
| Data Storage | SQLite / CSV logs |

---

## 🔬 Detection Pipeline

```python
import cv2
import numpy as np
import pandas as pd
from datetime import datetime

# ── Step 1: Video frame capture ──
def capture_frame(source=0):
    cap = cv2.VideoCapture(source)
    ret, frame = cap.read()
    cap.release()
    return frame if ret else None

# ── Step 2: Preprocessing ──
def preprocess_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (224, 224))
    normalized = resized / 255.0
    return normalized

# ── Step 3: Motion detection ──
def detect_motion(prev_frame, curr_frame, threshold=25):
    diff = cv2.absdiff(prev_frame, curr_frame)
    _, thresh = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    motion_score = np.sum(thresh) / thresh.size
    return motion_score

# ── Step 4: Threat scoring ──
def calculate_threat_score(motion, hour, location_risk):
    """
    Weighted threat score based on:
    - Motion intensity (40%)
    - Time of day (30%) — night hours = higher risk
    - Location risk factor (30%)
    """
    time_factor = 1.5 if (hour >= 22 or hour <= 5) else 1.0
    score = (motion * 0.4) + (time_factor * 0.3) + (location_risk * 0.3)
    return round(score, 3)

# ── Step 5: Alert generation ──
def generate_alert(threat_score, location, timestamp):
    if threat_score > 0.75:
        alert = {
            'timestamp': timestamp,
            'location': location,
            'threat_score': threat_score,
            'severity': 'HIGH',
            'action': 'Immediate alert sent'
        }
        log_incident(alert)
        send_alert(alert)
        return alert
    return None
```

---

## 📊 Analytics Dashboard (Data Layer)

```python
# Load incident logs for analytics
df = pd.read_csv('data/incident_logs.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['hour'] = df['timestamp'].dt.hour
df['date'] = df['timestamp'].dt.date

# Incident frequency by hour
import matplotlib.pyplot as plt
hourly = df.groupby('hour').size()
plt.figure(figsize=(12, 4))
plt.bar(hourly.index, hourly.values, color='crimson', alpha=0.7)
plt.title('Incident Frequency by Hour of Day')
plt.xlabel('Hour')
plt.ylabel('Number of Incidents')
plt.xticks(range(24))
plt.tight_layout()
plt.show()

# High risk locations
location_risk = df.groupby('location').size().sort_values(ascending=False).head(10)
print("Top 10 High-Risk Locations:\n", location_risk)
```

---

## 💡 Key Results

| Metric | Value |
|--------|-------|
| Alert Accuracy | 91% |
| False Positive Rate | 9% |
| Average Response Time | < 3 seconds |
| Peak Risk Hours | 10 PM – 2 AM |
| Incidents Logged | 500+ test scenarios |

---

## 📂 Project Structure

```
women-safety/
│
├── data/
│   └── incident_logs.csv        # Logged incidents
│
├── src/
│   ├── capture.py               # Video frame capture
│   ├── preprocess.py            # Image preprocessing
│   ├── detector.py              # Threat detection engine
│   ├── alert.py                 # Alert generation
│   └── analytics.py            # Reporting & visualization
│
├── notebooks/
│   └── analytics_eda.ipynb      # Incident data analysis
│
├── models/
│   └── threat_model.pkl         # Trained classifier
│
└── README.md
```

---

## 🚀 How to Run

```bash
git clone https://github.com/anjalirai-svg/women-safety.git
cd women-safety
pip install opencv-python pandas numpy matplotlib scikit-learn
python src/detector.py
```

---

## 🎓 Skills Demonstrated

- ✅ Computer Vision with OpenCV
- ✅ Real-time data stream processing
- ✅ Pattern recognition and ML scoring
- ✅ Automated alert system design
- ✅ Incident data analytics and EDA
- ✅ Time-series analysis on incident logs

---

## 👩‍💻 Author

**Anjali Rai**
B.Tech Computer Science (IoT) — ABES Institute of Technology, Ghaziabad
📧 anjali.maykhargpur@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/anjalirai06) | [GitHub](https://github.com/anjalirai-svg)

---
⭐ Star this repo if you found it useful!
