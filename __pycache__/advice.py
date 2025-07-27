import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env file

API_KEY = os.getenv("HEALTH_TIPS_API_KEY")
API_URL = "https://example-health-tips-api.p.rapidapi.com/tips"  # Replace with real API URL

STATIC_TIPS = {
    "Low": [
        "If your heart rate is low, avoid sudden exertion.",
        "Keep track of any dizziness or fatigue.",
        "Consult your doctor if symptoms persist."
    ],
    "Normal": [
        "Maintain a balanced diet and regular exercise.",
        "Stay hydrated and manage stress.",
        "Regular checkups keep your heart healthy."
    ],
    "High": [
        "Avoid caffeine and stressful situations.",
        "Practice relaxation and breathing exercises.",
        "If your heart rate stays high, seek medical advice."
    ],
    "Invalid": [
        "Please enter a valid heart rate next time."
    ]
}

def fetch_health_tips(status):
    """
    Fetch health tips based on heart rate status from an external API.
    If API fails or no API key, return static tips as fallback.
    """
    if not API_KEY:
        # No API key found, use static tips
        return STATIC_TIPS.get(status, ["No tips available."])

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "example-health-tips-api.p.rapidapi.com"
    }
    params = {"condition": status.lower()}  # API expects condition param

    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        # Assume API returns tips as list of strings in 'tips' field
        tips = data.get("tips")
        if tips:
            return tips
        else:
            return STATIC_TIPS.get(status, ["No tips available."])
    except Exception as e:
        # API call failed — fallback to static tips
        print(f"⚠️ Warning: Could not fetch tips from API ({e})")
        return STATIC_TIPS.get(status, ["No tips available."])
