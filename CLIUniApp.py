from colorama import Fore, Style, init
from controllers.student_controller import StudentController
from controllers.admin_controller import AdminController

init(autoreset=True)


def main():
    student_ctrl = StudentController()
    admin_ctrl = AdminController()

    while True:
        choice = input(Fore.CYAN + "University System: (A)dmin, (S)tudent, or X : " + Style.RESET_ALL).strip().upper()
        if choice == 'A':
            admin_ctrl.run()
        elif choice == 'S':
            student_ctrl.run()
        elif choice == 'X':
            print(Fore.YELLOW + "Thank You")
            break


if __name__ == "__main__":
    main()
