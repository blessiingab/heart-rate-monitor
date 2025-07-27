def check_heart_rate(bpm):
    if bpm < 60:
        return "Low"
    elif 60 <= bpm <= 100:
        return "Normal"
    elif bpm > 100:
        return "High"
    else:
        return "Invalid"
