"""
Gesture Analysis Module
Uses MediaPipe Pose to detect distress-related gestures/postures,
e.g. raised arms (SOS-like signal) or sudden erratic movement.
"""

import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose


class GestureAnalyzer:
    def __init__(self, detection_confidence: float = 0.5):
        self.pose = mp_pose.Pose(
            static_image_mode=False,
            min_detection_confidence=detection_confidence
        )
        self._prev_wrist_y = None

    def analyze(self, cropped_person_frame: np.ndarray) -> dict:
        """
        Returns a dict with basic distress signal flags:
        {"arms_raised": bool, "rapid_movement": bool}
        """
        result = {"arms_raised": False, "rapid_movement": False}

        if cropped_person_frame is None or cropped_person_frame.size == 0:
            return result

        rgb_frame = cropped_person_frame[:, :, ::-1]  # BGR -> RGB
        pose_result = self.pose.process(rgb_frame)

        if not pose_result.pose_landmarks:
            return result

        landmarks = pose_result.pose_landmarks.landmark
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
        left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
        right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]

        # Arms raised: wrists above shoulders (lower y = higher in image)
        if left_wrist.y < left_shoulder.y and right_wrist.y < right_shoulder.y:
            result["arms_raised"] = True

        # Rapid movement heuristic based on wrist y-position delta between frames
        avg_wrist_y = (left_wrist.y + right_wrist.y) / 2
        if self._prev_wrist_y is not None:
            delta = abs(avg_wrist_y - self._prev_wrist_y)
            if delta > 0.15:  # tune threshold based on frame rate/resolution
                result["rapid_movement"] = True
        self._prev_wrist_y = avg_wrist_y

        return result

    def close(self):
        self.pose.close()
