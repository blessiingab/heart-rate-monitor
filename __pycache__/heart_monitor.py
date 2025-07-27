#!/usr/bin/env python3

from evaluator import check_heart_rate
from advice import fetch_health_tips

def main():
    print("=== Heart Rate Monitor with Health Tips ===")
    try:
        bpm = int(input("Enter your resting heart rate (bpm): "))
        status = check_heart_rate(bpm)
        print(f"\nStatus: {status}")

        # Get relevant health tips from external API (or fallback)
        tips = fetch_health_tips(status)
        print("\n💡 Health Tips for you:")
        for i, tip in enumerate(tips, 1):
            print(f"{i}. {tip}")

    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
# This script monitors heart rate and provides health tips based on the input.
