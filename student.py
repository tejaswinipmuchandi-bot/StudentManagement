def main():
    print("STUDENT MANAGEMENT SYSTEM")

    name = input("Enter student name: ")
    program = input("Enter program: ")
    semester = input("Enter semester: ")

    courses = []

    count = int(input("Enter number of courses: "))

    for i in range(count):
        print("Course", i + 1)

        course_name = input("Enter course name: ")
        marks = float(input("Enter marks (0-100): "))

        while marks < 0 or marks > 100:
            print("Please enter marks between 0 and 100.")
            marks = float(input("Enter marks (0-100): "))

        courses.append((course_name, marks))

    print("========== STUDENT REPORT ==========")
    print("Name:", name)
    print("Program:", program)
    print("Semester:", semester)

    print("Course Details:")

    for course_name, marks in courses:
        print(course_name, ":", marks)

    below_pass = [
        course_name for course_name, marks in courses if marks < 50
    ]

    if below_pass:
        print("Courses with marks below 50:")
        for course_name in below_pass:
            print("-", course_name)
    else:
        print("No courses below 50 marks.")


if __name__ == "__main__":
    main()