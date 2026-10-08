from validation import validate_mark
from calculation import calculate_tootal, calculate_average, calculate_grade
from display import display_result

def main():
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {i+1}: "))
                if validate_mark(mark):
                    marks.append(mark)
                    break
                else:
                    print("Invalid marks. Enter 0-100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    total = calculate_tootal(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)

    display_result(name, total, average, grade)

if __name__ == "__main__":
    main()