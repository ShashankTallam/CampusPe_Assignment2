
def personal_bio_card():

    # Step 1: Store student information in variables
    student_name = "T J Shashank"
    student_age = 21
    enrolled_course = "Python Programming"
    college_name = "ABC University"
    email_address = "shashank@example.com"

    # Step 2: Prepare lines to print inside the box
    details = [
        f"Name    : {student_name}",
        f"Age     : {student_age} years",
        f"Course  : {enrolled_course}",
        f"College : {college_name}",
        f"Email   : {email_address}"
    ]

    # Step 3: Decide box width 
    title = "STUDENT BIO CARD"
    content_width = max(len(title), *(len(line) for line in details)) + 4

    # Step 4: Print top border and title row
    print("╔" + "═" * content_width + "╗")
    print(f"║{title:^{content_width}}║")

    # Step 5: Print title separator line
    print("╠" + "═" * content_width + "╣")

    # Step 6: Print each detail inside the box
    for line in details:
        print(f"║ {line:<{content_width - 2}} ║")

    # Step 7: Print bottom border
    print("╚" + "═" * content_width +  "╝")


# Calling the function 
personal_bio_card()