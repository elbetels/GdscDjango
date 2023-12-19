
student_db = {}


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    student_db[name] = {
        'age': age,
        'grade': grade
    }
    print("Student added successfully.")


def view_student():
    name = input("Enter student name: ")
   
    if name in student_db:
        student = student_db[name]
        print("Name:", name)
        print("Age:", student['age'])
        print("Grade:", student['grade'])
    else:
        print("Student not found.")

def list_students():
    print("List of students:")
    for name, student in student_db.items():
        print("Name:", name)
        print("Age:", student['age'])
        print("Grade:", student['grade'])
        print("-----------------------")

def update_student():
    name = input("Enter student name: ")
    if name in student_db:
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")
        student_db[name]['age'] = age
        student_db[name]['grade'] = grade
        print("Student information updated successfully.")
    else:
        print("Student not found.")

def delete_student():
    name = input("Enter student name: ")

    if name in student_db:
       
        del student_db[name]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

while True:
    print("\nStudent Database")
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Quit")
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_student()
    elif choice == '3':
        list_students()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")