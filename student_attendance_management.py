# STUDENT ATTENDANCE MANAGEMENT SYSTEM
# FY B.Tech Python Mini Project

from datetime import datetime

students = {}
attendance_records = []

print("=" * 45)
print("       STUDENT ATTENDANCE MANAGEMENT")
print("=" * 45)

while True:
    print("\nMAIN MENU")
    print("1. Add student")
    print("2. Mark attendance")
    print("3. View attendance")
    print("4. View attendance summary")
    print("5. Save attendance report")
    print("0. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        roll_no = input("Enter student roll number: ").strip()
        name = input("Enter student name: ").strip()

        if not roll_no or not name:
            print("Roll number and name cannot be empty.")
        elif roll_no in students:
            print("This roll number already exists.")
        else:
            students[roll_no] = name
            print("Student added successfully.")

    elif choice == 2:
        if not students:
            print("Please add students first.")
            continue

        today = datetime.now().strftime("%d-%m-%Y")
        print("\nDate:", today)

        for roll_no, name in students.items():
            status = input(
                f"Is {name} (Roll No. {roll_no}) present? (P/A): "
            ).strip().upper()

            while status not in ("P", "A"):
                print("Enter P for Present or A for Absent.")
                status = input("Enter attendance (P/A): ").strip().upper()

            attendance_records.append(
                [today, roll_no, name, "Present" if status == "P" else "Absent"]
            )

        print("Attendance marked successfully.")

    elif choice == 3:
        if not attendance_records:
            print("No attendance records available.")
        else:
            print("\nATTENDANCE RECORDS")
            print("-" * 65)
            for record in attendance_records:
                print(
                    "Date:", record[0],
                    "| Roll No.:", record[1],
                    "| Name:", record[2],
                    "| Status:", record[3]
                )

    elif choice == 4:
        if not students:
            print("No students have been added.")
        else:
            print("\nATTENDANCE SUMMARY")
            print("-" * 45)

            for roll_no, name in students.items():
                records = [
                    record for record in attendance_records
                    if record[1] == roll_no
                ]
                present = sum(1 for record in records if record[3] == "Present")
                absent = sum(1 for record in records if record[3] == "Absent")
                total_days = present + absent

                if total_days > 0:
                    percentage = (present / total_days) * 100
                else:
                    percentage = 0

                print(f"Name: {name} | Roll No.: {roll_no}")
                print(
                    f"Present: {present} | Absent: {absent} | "
                    f"Attendance: {percentage:.1f}%"
                )
                print("-" * 45)

    elif choice == 5:
        filename = "attendance_report.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write("STUDENT ATTENDANCE REPORT\n")
            file.write("Generated: " + datetime.now().strftime("%d-%m-%Y %H:%M") + "\n")
            file.write("=" * 60 + "\n")

            for record in attendance_records:
                file.write(
                    f"Date: {record[0]} | Roll No.: {record[1]} | "
                    f"Name: {record[2]} | Status: {record[3]}\n"
                )

            file.write("\nATTENDANCE SUMMARY\n")
            for roll_no, name in students.items():
                records = [
                    record for record in attendance_records
                    if record[1] == roll_no
                ]
                present = sum(1 for record in records if record[3] == "Present")
                absent = sum(1 for record in records if record[3] == "Absent")
                total_days = present + absent
                percentage = (present / total_days * 100) if total_days else 0

                file.write(
                    f"{name} ({roll_no}): Present={present}, "
                    f"Absent={absent}, Attendance={percentage:.1f}%\n"
                )

        print("Attendance report saved as", filename)

    elif choice == 0:
        print("Thank you for using the Attendance Management System!")
        break

    else:
        print("Invalid choice. Please select an option from the menu.")
