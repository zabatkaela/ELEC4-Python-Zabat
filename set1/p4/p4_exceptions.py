# Name: KAELA ASHLEY NICOLE R. ZABAT
# Section: IV-BSIT C
# Activity: P4 - Safe Menu Program
# Date: November 15, 2026

while True:
    print("\n--- SAFE MENU PROGRAM ---")
    print("1. Divide Numbers")
    print("2. Open File")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 / num2

        except ValueError:
            print("Error: Please enter valid numbers.")

        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")

        else:
            print("Result:", result)

        finally:
            print("Division operation finished.")

    elif choice == "2":
        filename = input("Enter file name: ")

        try:
            with open(filename, "r") as file:
                content = file.read()

        except FileNotFoundError:
            print("Error: File not found.")

        else:
            print("\n--- FILE CONTENT ---")
            print(content)

        finally:
            print("File operation finished.")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")