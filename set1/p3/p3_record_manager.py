# Name: KAELA ASHLEY NICOLE R. ZABAT
# Section: IV-BSIT C
# Activity: P3 - Student Record Manager
# Date: November 15, 2026

students = []
student_set = set()

# Add a student
def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
    elif name.lower() in student_set:
        print("Student already exists!")
    else:
        students.append(name)
        student_set.add(name.lower())
        print("Student added successfully!")


# Remove a student
def remove_student():
    name = input("Enter name to remove: ").strip().lower()

    for student in students:
        if student.lower() == name:
            students.remove(student)
            student_set.remove(name)
            print("Student removed successfully!")
            return

    print("Student not found!")


# Search for a student
def search_student():
    name = input("Enter name to search: ").strip().lower()

    found = False

    for student in students:
        if name in student.lower():
            print("Found:", student)
            found = True

    if not found:
        print("Student not found!")


# Display all students
def display_students():
    if not students:
        print("No students found.")
        return

    print("\n--- STUDENT LIST ---")

    for number, name in enumerate(sorted(students, key=str.lower), 1):
        print(f"{number}. {name}")

    print("Total Students:", len(students))


# Main menu
while True:
    print("\n--- STUDENT RECORD MANAGER ---")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        display_students()
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid option!")


# A list stores student names and allows duplicate values.
# A set stores unique values and prevents duplicates.
# I used a list to keep and display student names.
# I used a set to check if a student already exists.
# Both collections help manage the student records.