from controllers.student_controller import StudentController
from controllers.admin_controller import AdminController


def main():
    student_ctrl = StudentController()
    admin_ctrl = AdminController()

    while True:
        choice = input("University System: (A)dmin, (S)tudent, or X : ").strip().upper()
        if choice == 'A':
            admin_ctrl.run()
        elif choice == 'S':
            student_ctrl.run()
        elif choice == 'X':
            print("Thank You")
            break


if __name__ == "__main__":
    main()
