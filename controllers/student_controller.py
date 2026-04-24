import re
from models.student import Student
from models.database import Database
from controllers.subject_controller import SubjectController, validate_credentials

INDENT = "        "

EMAIL_PATTERN = re.compile(r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$')
PASSWORD_PATTERN = re.compile(r'^[A-Z][a-zA-Z]{5,}\d{3,}$')


class StudentController:
    def run(self):
        while True:
            choice = input(f"{INDENT}Student System (l/r/x): ").strip().lower()
            if choice == 'l':
                self._login()
            elif choice == 'r':
                self._register()
            elif choice == 'x':
                break

    def _register(self):
        print(f"{INDENT}Student Sign Up")
        while True:
            email = input(f"{INDENT}Email: ").strip()
            password = input(f"{INDENT}Password: ").strip()
            if not validate_credentials(email, password):
                print(f"{INDENT}Incorrect email or password format")
                continue
            print(f"{INDENT}email and password formats acceptable")
            students = Database.load()
            existing = next((s for s in students if s.email == email), None)
            if existing:
                print(f"{INDENT}Student {existing.name} already exists")
                return
            name = input(f"{INDENT}Name: ").strip()
            student = Student(name, email, password)
            print(f"{INDENT}Enrolling Student {student.name}")
            students.append(student)
            Database.save(students)
            return

    def _login(self):
        print(f"{INDENT}Student Sign In")
        while True:
            email = input(f"{INDENT}Email: ").strip()
            password = input(f"{INDENT}Password: ").strip()
            if not validate_credentials(email, password):
                print(f"{INDENT}Incorrect email or password format")
                continue
            print(f"{INDENT}email and password formats acceptable")
            students = Database.load()
            student = next((s for s in students if s.email == email and s.password == password), None)
            if not student:
                print(f"{INDENT}Student does not exist")
                return
            SubjectController(student).run()
            return
