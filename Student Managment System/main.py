# Student Management System 

Student_grades = {}


# use function for add_Student 

def add_student(name , grade):
    Student_grades[name] = grade
    print(f"Added {name} With a {grade}")

# use function for update_Student 
def upd_student(name , grade):
    if name in Student_grades:
        Student_grades[name] = grade
        print(f"{name} with update marks {grade}")
    else:
        print(f"{name} is not Found !")

# use function for Delete_Student 
def delete_student(name):
    if name in Student_grades:
        del Student_grades[name]
        print(f" {name} , deleted Student Name")
    else:
        print(f"{name} is not Found !")
        
# View All Student name
def display_all_student():
    if Student_grades:
        for name , grade in Student_grades.items():
            print(f"{name} {grade}")

    else:
        print("No student found ! ")



def main():
    while True:
        print("\n--------------------- Student Grade management System ------------------")
        print("1. Add Student")
        print("2. update Student")
        print("3. Deleted Student")
        print("4. View all Student")
        print("5. Exit")

        choice = int(input("Choice any one you want : "))

        if choice == 1:
            name = input("Enter a Name of Student : ")
            grade = int(input("Enter a grade of Student : "))
            add_student(name,grade)
        elif choice == 2:
            name = input("Enter a Name of Student : ")
            grade = int(input("Enter a Updated grade of Student : "))
            upd_student(name,grade)

        elif choice == 3:
            name = input("Enter a Name of Student : ")
            delete_student(name)

        elif choice == 4:
            print("\n-----------------All Student-------------")
            display_all_student()

        elif choice == 5:
            print("-------------------Thankyou For use my System--------------")
            break
        else:
            print("You click worng Number ! ")


main()
    