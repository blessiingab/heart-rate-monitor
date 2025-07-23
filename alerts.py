#!/usr/bin/env python3
# alerts.py

def check_alert(bpm):
    if bpm < 50:
        return "⚠️ Low heart rate detected!"
    elif bpm > 100:
        return "⚠️ High heart rate detected!"
    return None

