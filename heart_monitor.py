#!/usr/bin/env python3
# heart_monitor.py
from models import Session, Person, HeartRate
from alerts import check_alert

def register_person():
    session = Session()
    name = input("Enter full name: ")
    email = input("Enter email: ")
    gender = input("Gender (M/F): ").upper()
    person = Person(name=name, email=email, gender=gender)
    session.add(person)
    session.commit()
    print("\u2705 Registered successfully.\n")
    session.close()

def record_heart_rate():
    session = Session()
    email = input("Enter email of the person: ")
    person = session.query(Person).filter_by(email=email).first()

    if not person:
        print("\u274c Person not found.\n")
        return

    bpm = float(input("Enter BPM: "))
    reading = HeartRate(person_id=person.id, bpm=bpm)
    session.add(reading)
    session.commit()
    print("\u2705 Heart rate recorded.\n")

    alert = check_alert(bpm)
    if alert:
        print(alert)

    session.close()

def view_records():
    session = Session()
    email = input("Enter email: ")
    person = session.query(Person).filter_by(email=email).first()

    if not person:
        print("\u274c Person not found.")
        return

    print(f"\n\ud83d\udcc4 Heart Rate Records for {person.name}")
    for r in person.readings:
        print(f"{r.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {r.bpm} BPM")
    session.close()

def main():
    while True:
        print("\n\ud83d\udc93 HEART RATE MONITOR")
        print("1. Register person")
        print("2. Record heart rate")
        print("3. View records")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            register_person()
        elif choice == '2':
            record_heart_rate()
        elif choice == '3':
            view_records()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("\u2757 Invalid choice")

if __name__ == "__main__":
    main()

