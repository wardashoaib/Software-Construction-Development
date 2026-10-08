def calculate_total_marks(marks):
    return sum(marks)


def calculate_average_marks(total, marks):
    return total / len(marks)


def determine_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"


def display_result(name, total, average, grade):
    print("Name:", name)
    print("Total:", total)
    print("Average:", average)
    print("Grade:", grade)


def save_result(name, grade):
    with open("results.txt", "a") as file:
        file.write(f"{name}: {grade}\n")


name = "Ali"
marks = [80, 75, 90]

total = calculate_total_marks(marks)
average = calculate_average_marks(total, marks)
grade = determine_grade(average)

display_result(name, total, average, grade)
save_result(name, grade)