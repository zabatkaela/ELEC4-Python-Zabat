# Name: KAELA ASHLEY NICOLE R. ZABAT
# Section: IV-BSIT C
# Activity: P2 - Custom Module
# Date: November 15, 2026

# Import custom and built-in modules
import student_utils
from student_utils import status
from datetime import datetime

grades = []

# Enter student grades
while True:
    try:
        grade = float(input("Enter grade (0-100): "))

        if 0 <= grade <= 100:
            grades.append(grade)
        else:
            print("Invalid grade! Enter 0-100.")
            continue

        while True:
            again = input("Add another grade? (y/n): ").lower()
            if again == "y" or again == "n":
                break
            print("Please enter y or n.")

        if again == "n":
            break

    except ValueError:
        print("Please enter a valid number.")

# Display student grade report
print("\n--- STUDENT GRADE REPORT ---")
print("Date:", datetime.now().strftime("%B %d, %Y"))
print("Average:", round(student_utils.average(grades), 2))
print("Highest:", student_utils.highest(grades))
print("Lowest:", student_utils.lowest(grades))
print("Status:", status(grades))