class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def accept_student(self, id, name, grade):
        self.students.append(Student(id, name, grade))

    def display_students(self):
        for student in self.students:
            print(f'ID: {student.id}, Name: {student.name}, Grade: {student.grade}')

    def search_student(self, id):
        for student in self.students:
            if student.id == id:
                return student
        return None

    def delete_student(self, id):
        self.students = [student for student in self.students if student.id != id]

    def update_student(self, id, name=None, grade=None):
        for student in self.students:
            if student.id == id:
                if name:
                    student.name = name
                if grade:
                    student.grade = grade

def main():
    sms = StudentManagementSystem()
    while True:
        print("1. Accept Student details")
        print("2. Display Student Details")
        print("3. Search Details of a Student")
        print("4. Delete Details of Student")
        print("5. Update Student Details")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            id = input("Enter student id: ")
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            sms.accept_student(id, name, grade)
        elif choice == 2:
            sms.display_students()
        elif choice == 3:
            id = input("Enter student id: ")
            student = sms.search_student(id)
            if student:
                print(f'ID: {student.id}, Name: {student.name}, Grade: {student.grade}')
            else:
                print("Student not found")
        elif choice == 4:
            id = input("Enter student id: ")
            sms.delete_student(id)
        elif choice == 5:
            id = input("Enter student id: ")
            name = input("Enter new student name (leave blank to keep the same): ")
            grade = input("Enter new student grade (leave blank to keep the same): ")
            sms.update_student(id, name, grade)
        elif choice == 6:
            break

if __name__ == "__main__":
    main()
