# Ethical & Privacy Considerations

This project detects and analyzes people in video streams. That comes with real responsibilities before any real-world or public deployment.

## Key Considerations

1. **Consent & Legal Compliance**
   - Public camera surveillance is regulated differently across jurisdictions. Confirm compliance with local laws (e.g. data protection acts, surveillance regulations) before deployment.
   - Where feasible, post clear signage indicating monitored areas.

2. **Bias & Fairness**
   - Gender classification models can carry significant bias across skin tones, clothing styles, and cultural contexts. Any classifier used here must be validated against diverse, representative datasets and audited for disparate error rates before use.
   - Avoid over-reliance on appearance-based inference — treat model outputs as probabilistic signals, not ground truth.

3. **False Positives / False Negatives**
   - Risk-scoring logic in `alert_manager.py` is a simple rule-based placeholder. It will produce false alarms (e.g. flagging normal group gatherings) and missed detections. Human review should always be in the loop before any action is taken based on an alert.

4. **Data Minimization & Retention**
   - Avoid storing raw video/images longer than necessary. This reference implementation logs only aggregate metadata (counts, risk level, timestamp) — not identifiable images — by design. Keep it that way unless you have a specific, lawful, and consented reason to store more.

5. **No Individual Profiling**
   - This system is designed for aggregate, situational risk signals (e.g. "a lone woman is present at night in this area"), not for tracking or profiling specific individuals across time or locations.

6. **Human Oversight**
   - This tool is a decision-support aid for control-room staff or authorities — not an autonomous enforcement system. All alerts should be reviewed by a human before any action is taken.

## Recommended Before Deployment

- Conduct a formal privacy impact assessment (PIA).
- Have the model bias-audited by an independent party.
- Pilot in a controlled setting with stakeholder (including community) input before scaling up.
