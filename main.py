"""
Main Entry Point
Orchestrates the video stream -> detection -> gesture analysis ->
risk assessment -> alerting pipeline.
"""

import argparse
from datetime import datetime

import cv2

from stream_processor import StreamProcessor
from detection import PersonDetector, GenderClassifier, crop_box
from gesture_analysis import GestureAnalyzer
from alert_manager import AlertManager


def parse_args():
    parser = argparse.ArgumentParser(description="Women Safety Analytics Pipeline")
    parser.add_argument("--source", default=0, help="Video source: 0 for webcam, or RTSP/file path")
    parser.add_argument("--model", default="models/yolov8n.pt", help="Path to YOLOv8 model weights")
    parser.add_argument("--show", action="store_true", help="Display annotated video window")
    return parser.parse_args()


def main():
    args = parse_args()
    source = int(args.source) if str(args.source).isdigit() else args.source

    stream = StreamProcessor(source=source)
    detector = PersonDetector(model_path=args.model)
    gender_classifier = GenderClassifier()
    gesture_analyzer = GestureAnalyzer()
    alert_manager = AlertManager()

    print("Starting Women Safety Analytics pipeline... Press 'q' to quit (if --show enabled).")

    try:
        for frame in stream.frames():
            boxes = detector.detect(frame)
            person_count = len(boxes)
            female_count = 0
            distress_flags = []

            for box in boxes:
                cropped = crop_box(frame, box)
                gender = gender_classifier.predict(cropped)
                if gender == "female":
                    female_count += 1

                gesture_result = gesture_analyzer.analyze(cropped)
                distress_flags.append(gesture_result["arms_raised"] or gesture_result["rapid_movement"])

                if args.show:
                    x1, y1, x2, y2, conf = box
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            hour = datetime.now().hour
            assessment = alert_manager.evaluate(person_count, female_count, distress_flags, hour)
            alert_manager.trigger_alert(assessment)

            if args.show:
                cv2.imshow("Women Safety Analytics", frame)
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

    finally:
        stream.release()
        gesture_analyzer.close()
        if args.show:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
