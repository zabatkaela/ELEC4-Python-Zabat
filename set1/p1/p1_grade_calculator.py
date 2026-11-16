# Name: KAELA ASHLEY NICOLE R. ZABAT
# Section: IV-BSIT-C
# Activity: P1 - Student Grade Calculator
# Date: November 15, 2026

def enter_grades():
    grades = []

    while True:
        try:
            grade = float(input("Enter grade (0-100): "))

            if grade >= 0 and grade <= 100:
                grades.append(grade)
            else:
                print("Invalid grade! Enter 0-100.")
                continue

            again = input("Add another grade? (y/n): ").lower()
            if again == "n":
                break

        except ValueError:
            print("Please enter a valid number.")

    return grades


def get_average(grades):
    return sum(grades) / len(grades)


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)


def get_status(grades):
    if get_average(grades) >= 75:
        return "PASSED"
    else:
        return "FAILED"


grades = []

while True:
    print("\n--- STUDENT GRADE CALCULATOR ---")
    print("1. Enter Grades")
    print("2. View Results")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        grades = enter_grades()

    elif choice == "2":
        if len(grades) == 0:
            print("No grades entered yet.")
        else:
            print("\n--- GRADE RESULTS ---")
            print("Average:", round(get_average(grades), 2))
            print("Highest:", get_highest(grades))
            print("Lowest:", get_lowest(grades))
            print("Status:", get_status(grades))

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Try again.")


# A local variable is created inside a function.
# The grade variable in enter_grades() is a local variable.
# A global variable is created outside the functions.
# The grades variable before the main menu is a global variable.