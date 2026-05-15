import re
from colorama import Fore, Style
from models.subject import Subject
from models.database import Database

INDENT = "        "
MAX_SUBJECTS = 4

EMAIL_PATTERN    = re.compile(r'^[a-zA-Z]+\.[a-zA-Z]+@university\.com$')
PASSWORD_PATTERN = re.compile(r'^[A-Z][a-zA-Z]{5,}\d{3,}$')


def validate_credentials(email, password):
    return bool(EMAIL_PATTERN.match(email)) and bool(PASSWORD_PATTERN.match(password))


class SubjectController:
    def __init__(self, student):
        self.student = student

    def run(self):
        while True:
            choice = input(Fore.CYAN + f"{INDENT}Student Course Menu (c/e/r/s/x): " + Style.RESET_ALL).strip().lower()
            if choice == 'c':
                self._change_password()
            elif choice == 'e':
                self._enrol()
            elif choice == 'r':
                self._remove_subject()
            elif choice == 's':
                self._show_subjects()
            elif choice == 'x':
                break

    def _enrol(self):
        if len(self.student.subjects) >= MAX_SUBJECTS:
            print(Fore.RED + f"{INDENT}Students are allowed to enrol in 4 subjects only")
            return
        subject = Subject()
        existing_ids = {s.id for s in self.student.subjects}
        while subject.id in existing_ids:
            subject = Subject()
        self.student.subjects.append(subject)
        print(Fore.YELLOW + f"{INDENT}Enrolling in Subject-{int(subject.id)}")
        print(Fore.YELLOW + f"{INDENT}You are now enrolled in {len(self.student.subjects)} out of 4 subjects")
        self._save()

    def _remove_subject(self):
        subject_id        = input(Fore.CYAN + f"{INDENT}Remove Subject by ID: " + Style.RESET_ALL).strip()
        subject_id_padded = f"{int(subject_id):03d}" if subject_id.isdigit() else subject_id
        for subject in self.student.subjects:
            if subject.id == subject_id_padded:
                self.student.subjects.remove(subject)
                print(Fore.YELLOW + f"{INDENT}Droping Subject-{int(subject_id_padded)}")
                print(Fore.YELLOW + f"{INDENT}You are now enrolled in {len(self.student.subjects)} out of 4 subjects")
                self._save()
                return
        print(Fore.RED + f"{INDENT}Subject not found")

    def _show_subjects(self):
        print(Fore.YELLOW + f"{INDENT}Showing {len(self.student.subjects)} subjects")
        for subject in self.student.subjects:
            print(f"{INDENT}{subject}")

    def _change_password(self):
        print(Fore.YELLOW + f"{INDENT}Updating Password")
        while True:
            new_password = input(f"{INDENT}New Password: ").strip()
            if not validate_credentials(self.student.email, new_password):
                print(Fore.RED + f"{INDENT}Incorrect password format")
                continue
            while True:
                confirm = input(f"{INDENT}Confirm Password: ").strip()
                if confirm == new_password:
                    self.student.password = new_password
                    self._save()
                    break
                print(Fore.RED + f"{INDENT}Password does not match - try again")
            break

    def _save(self):
        students = Database.load()
        for i, s in enumerate(students):
            if s.id == self.student.id:
                students[i] = self.student
                break
        Database.save(students)
