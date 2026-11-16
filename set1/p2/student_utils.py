# Name: KAELA ASHLEY NICOLE R. ZABAT
# Section: IV-BSIT C
# Activity: P2 - Custom Module
# Date: November 15, 2026

# Calculate the average grade
def average(grades):
    return sum(grades) / len(grades)

# Check if the student passed
def status(grades):
    if average(grades) >= 75:
        return "PASSED"
    else:
        return "FAILED"

# Get the highest grade
def highest(grades):
    return max(grades)

# Get the lowest grade
def lowest(grades):
    return min(grades)