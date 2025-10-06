import json

FILE_NAME = "students.json"

# Load data
def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Add a new student
def add_student():
    data = load_data()
    roll = input("Enter Roll Number: ").strip()
    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()

    # Validation
    if not roll or not name or not age or not course:
        print("All fields are required!\n")
        return
    if not age.isdigit():
        print("Age must be a number!\n")
        return
    for s in data:
        if s["Roll"] == roll:
            print("Roll number already exists!\n")
            return

    student = {"Roll": roll, "Name": name, "Age": age, "Course": course}
    data.append(student)
    save_data(data)
    print("Student Added Successfully!\n")

# View all students
def view_students():
    data = load_data()
    if not data:
        print("No student records found.\n")
    else:
        print("\n--- Student Records ---")
        for s in data:
            print(f"Roll: {s['Roll']}, Name: {s['Name']}, Age: {s['Age']}, Course: {s['Course']}")
        print()

# Search for a student by roll number
def search_student():
    roll = input("Enter Roll Number to Search: ").strip()
    data = load_data()
    for s in data:
        if s["Roll"] == roll:
            print(f"\nFound Student Record:\nRoll: {s['Roll']}, Name: {s['Name']}, Age: {s['Age']}, Course: {s['Course']}\n")
            return
    print("Student not found.\n")

# Delete a student by roll number
def delete_student():
    roll = input("Enter Roll Number to Delete: ").strip()
    data = load_data()
    new_data = [s for s in data if s["Roll"] != roll]

    if len(data) == len(new_data):
        print("Student not found.\n")
    else:
        save_data(new_data)
        print("Student Deleted Successfully!\n")

# Main menu
def student_menu():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ").strip()
        print()  # for spacing

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting Student Management System. Goodbye!\n")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run program
if __name__ == "__main__":
    student_menu()
