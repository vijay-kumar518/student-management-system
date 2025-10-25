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

# student inform 
def add_student():
    data = load_data()
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    student = {"Roll": roll, "Name": name, "Age": age, "Course": course}
    data.append(student)
    save_data(data)
    print("✅ Student Added Successfully!\n")

def view_students():
    data = load_data()
    if not data:
        print("No student records found.\n")
    else:
        print("\n--- Student Records ---")
        for s in data:
            print(f"Roll: {s['Roll']}, Name: {s['Name']}, Age: {s['Age']}, Course: {s['Course']}")
        print()

# student search
def search_student():
    roll = input("Enter Roll Number to Search: ")
    data = load_data()
    for s in data:
        if s["Roll"] == roll:
            print(f"Found: {s}")
            return
    print("❌ Student not found.\n")

#student delete
def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    data = load_data()
    new_data = [s for s in data if s["Roll"] != roll]
    if len(data) == len(new_data):
        print("❌ Student not found.\n")
    else:
        save_data(new_data)
        print("✅ Student Deleted Successfully!\n")

# student menu
def student_menu():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice!\n")

# Run Student System
# student_menu()
