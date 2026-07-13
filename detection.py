"""
Detection Module
Runs person detection (YOLOv8) and aggregate gender classification
on each frame. Gender classifier is a placeholder - plug in a
properly trained, bias-audited model before real use.
"""

from ultralytics import YOLO
import numpy as np


class PersonDetector:
    def __init__(self, model_path: str = "models/yolov8n.pt", conf_threshold: float = 0.4):
        self.model = YOLO(model_path)
        self.conf_threshold = conf_threshold
        self.person_class_id = 0  # COCO class id for "person"

    def detect(self, frame: np.ndarray):
        """
        Returns a list of bounding boxes [(x1, y1, x2, y2, conf), ...]
        for detected persons in the frame.
        """
        results = self.model(frame, verbose=False)[0]
        boxes = []

        for box in results.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            if cls_id == self.person_class_id and conf >= self.conf_threshold:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                boxes.append((x1, y1, x2, y2, conf))

        return boxes


class GenderClassifier:
    """
    Placeholder aggregate gender classifier.
    Replace `predict` with a properly trained, bias-audited model.
    This is intentionally NOT wired to any real inference here —
    plug in your own model checkpoint before deployment.
    """

    def __init__(self, model_path: str = None):
        self.model_path = model_path
        # TODO: load your trained classifier here, e.g.:
        # self.model = load_model(model_path)

    def predict(self, cropped_person_frame: np.ndarray) -> str:
        """
        Returns "female", "male", or "unknown".
        Placeholder implementation - always returns "unknown"
        until a real model is integrated.
        """
        return "unknown"


def crop_box(frame: np.ndarray, box):
    x1, y1, x2, y2, _ = box
    return frame[max(0, y1):y2, max(0, x1):x2]
