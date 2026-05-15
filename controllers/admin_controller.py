from colorama import Fore, Style
from models.database import Database

INDENT = "        "


class AdminController:
    def run(self):
        while True:
            choice = input(Fore.CYAN + f"{INDENT}Admin System (c/g/p/r/s/x): " + Style.RESET_ALL).strip().lower()
            if choice == 'c':
                self._clear_database()
            elif choice == 'g':
                self._group_students()
            elif choice == 'p':
                self._partition_students()
            elif choice == 'r':
                self._remove_student()
            elif choice == 's':
                self._show_students()
            elif choice == 'x':
                break

    def _show_students(self):
        students = Database.load()
        print(Fore.YELLOW + f"{INDENT}Student List")
        if not students:
            print(f"{INDENT}< Nothing to Display >")
            return
        for s in students:
            print(f"{INDENT}{s.name} :: {s.id} --> Email: {s.email}")

    def _group_students(self):
        students = Database.load()
        print(Fore.YELLOW + f"{INDENT}Grade Grouping")
        if not students:
            print(f"{INDENT}< Nothing to Display >")
            return
        groups = {}
        for s in students:
            grade = s.get_grade()
            groups.setdefault(grade, []).append(s)
        grade_order = ['HD', 'D', 'C', 'P', 'F']
        for grade in grade_order:
            if grade in groups:
                entries = ', '.join(
                    f"{s.name} :: {s.id} --> GRADE: {s.get_grade():>2} - MARK: {s.get_average_mark():.2f}"
                    for s in groups[grade]
                )
                print(Fore.YELLOW + f"{INDENT}{grade} --> [{entries}]")

    def _partition_students(self):
        students = Database.load()
        print(Fore.YELLOW + f"{INDENT}PASS/FAIL Partition")
        passing  = [s for s in students if s.is_pass()]
        failing  = [s for s in students if not s.is_pass()]
        fail_str = ', '.join(
            f"{s.name} :: {s.id} --> GRADE: {s.get_grade():>2} - MARK: {s.get_average_mark():.2f}"
            for s in failing
        )
        pass_str = ', '.join(
            f"{s.name} :: {s.id} --> GRADE: {s.get_grade():>2} - MARK: {s.get_average_mark():.2f}"
            for s in passing
        )
        print(Fore.YELLOW + f"{INDENT}FAIL --> [{fail_str}]")
        print(Fore.YELLOW + f"{INDENT}PASS --> [{pass_str}]")

    def _remove_student(self):
        student_id = input(Fore.CYAN + f"{INDENT}Remove by ID: " + Style.RESET_ALL).strip()
        students   = Database.load()
        for s in students:
            if s.id == student_id:
                students.remove(s)
                Database.save(students)
                print(Fore.YELLOW + f"{INDENT}Removing Student {student_id} Account")
                return
        print(Fore.RED + f"{INDENT}Student {student_id} does not exist")

    def _clear_database(self):
        print(Fore.YELLOW + f"{INDENT}Clearing students database")
        confirm = input(Fore.RED + f"{INDENT}Are you sure you want to clear the database (Y)ES/(N)O: " + Style.RESET_ALL).strip().upper()
        if confirm == 'Y':
            Database.clear()
            print(Fore.YELLOW + f"{INDENT}Students data cleared")
