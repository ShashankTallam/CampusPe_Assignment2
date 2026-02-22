

def grade_calculator():
    try:
        marks_list = []

        # Take marks for 5 subjects
        for subject_number in range(1, 6):
            marks = float(input(f"Enter marks for subject {subject_number}: "))
            
            if marks < 0 or marks > 100:
                print("Marks should be between 0 and 100.")
                return
            
            marks_list.append(marks)

        total_marks = sum(marks_list)
        percentage = total_marks / 5

        # Determine grade
        if percentage >= 90:
            grade = "A+ (Outstanding)"
        elif percentage >= 80:
            grade = "A (Excellent)"
        elif percentage >= 70:
            grade = "B (Good)"
        elif percentage >= 60:
            grade = "C (Average)"
        elif percentage >= 50:
            grade = "D (pass)"
        else:
            grade = "F (Fail)"

        # Check pass or fail
        result_status = "Pass" if all(mark >= 40 for mark in marks_list) else "Fail"

        print("\n===== RESULT =====")
        print("Total Marks:", total_marks)
        print("Percentage:", percentage)
        print("Grade:", grade)
        print("Result:", result_status)

    except ValueError:
        print("Invalid input! Enter numeric values only.")
#calling the function
grade_calculator()