"""
Alert Manager
Handles risk-scoring logic based on detection + gesture signals,
logs incidents, and triggers alerts (console by default; extend
`trigger_alert` to hook into SMS/webhook/dashboard systems).
"""

import csv
import os
from datetime import datetime

INCIDENT_LOG = "incidents.csv"


class AlertManager:
    def __init__(self, log_file: str = INCIDENT_LOG):
        self.log_file = log_file
        self._init_log()

    def _init_log(self):
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "risk_level", "reason", "person_count", "female_count"])

    def evaluate(self, person_count: int, female_count: int, distress_flags: list, hour: int) -> dict:
        """
        Simple rule-based risk scoring. Extend with a trained model
        for production use.
        """
        risk_level = "low"
        reasons = []

        is_night = hour >= 21 or hour <= 5
        lone_woman = (person_count >= 1 and female_count == 1 and person_count == female_count)
        surrounded = (female_count == 1 and person_count - female_count >= 3)
        any_distress = any(distress_flags)

        if is_night and lone_woman:
            risk_level = "medium"
            reasons.append("Lone woman detected at night")

        if surrounded:
            risk_level = "high"
            reasons.append("Woman surrounded by a large group")

        if any_distress:
            risk_level = "high"
            reasons.append("Distress gesture detected")

        return {
            "risk_level": risk_level,
            "reasons": reasons,
            "person_count": person_count,
            "female_count": female_count,
        }

    def trigger_alert(self, assessment: dict):
        if assessment["risk_level"] in ("medium", "high"):
            self._log_incident(assessment)
            print(f"[ALERT - {assessment['risk_level'].upper()}] "
                  f"{', '.join(assessment['reasons'])} "
                  f"(persons={assessment['person_count']}, women={assessment['female_count']})")
            # TODO: hook into SMS/webhook/control-room dashboard here

    def _log_incident(self, assessment: dict):
        with open(self.log_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().isoformat(),
                assessment["risk_level"],
                "; ".join(assessment["reasons"]),
                assessment["person_count"],
                assessment["female_count"],
            ])
