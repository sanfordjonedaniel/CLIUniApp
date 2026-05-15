import re
from colorama import Fore, Style
from models.student import Student
from models.database import Database
from controllers.subject_controller import SubjectController, validate_credentials

INDENT = "        "

EMAIL_PATTERN = re.compile(r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$')
PASSWORD_PATTERN = re.compile(r'^[A-Z][a-zA-Z]{5,}\d{3,}$')


class StudentController:
    def run(self):
        while True:
            choice = input(Fore.CYAN + f"{INDENT}Student System (l/r/x): " + Style.RESET_ALL).strip().lower()
            if choice == 'l':
                self._login()
            elif choice == 'r':
                self._register()
            elif choice == 'x':
                break

    def _register(self):
        print(Fore.YELLOW + f"{INDENT}Student Sign Up")
        while True:
            email    = input(f"{INDENT}Email: ").strip()
            password = input(f"{INDENT}Password: ").strip()
            if not validate_credentials(email, password):
                print(Fore.RED + f"{INDENT}Incorrect email or password format")
                continue
            print(Fore.YELLOW + f"{INDENT}email and password formats acceptable")
            students = Database.load()
            existing = next((s for s in students if s.email == email), None)
            if existing:
                print(Fore.RED + f"{INDENT}Student {existing.name} already exists")
                return
            name = input(f"{INDENT}Name: ").strip()
            student = Student(name, email, password)
            print(Fore.YELLOW + f"{INDENT}Enrolling Student {student.name}")
            students.append(student)
            Database.save(students)
            return

    def _login(self):
        print(Fore.YELLOW + f"{INDENT}Student Sign In")
        while True:
            email    = input(f"{INDENT}Email: ").strip()
            password = input(f"{INDENT}Password: ").strip()
            if not validate_credentials(email, password):
                print(Fore.RED + f"{INDENT}Incorrect email or password format")
                continue
            print(Fore.YELLOW + f"{INDENT}email and password formats acceptable")
            students = Database.load()
            student  = next((s for s in students if s.email == email and s.password == password), None)
            if not student:
                print(Fore.RED + f"{INDENT}Student does not exist")
                return
            SubjectController(student).run()
            return
