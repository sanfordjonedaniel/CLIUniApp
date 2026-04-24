# CLIUniApp 🎓

A command-line university management system built in Python for UTS FEIT Assessment 1 – Part 2.  
It provides two interactive subsystems — one for **students** and one for **admins** — with all data persisted to a local `students.data` file.

---

## 📁 Project Structure

```
CLI Uni App/
├── CLIUniApp.py                  # Main entry point – University System menu
├── students.data                 # Auto-generated data file (pickle)
├── models/
│   ├── __init__.py
│   ├── subject.py                # Subject model (ID, mark, grade)
│   ├── student.py                # Student model (ID, name, email, password, subjects)
│   └── database.py               # Database handler (read / write / clear via pickle)
└── controllers/
    ├── __init__.py
    ├── student_controller.py     # Student System (register & login)
    ├── subject_controller.py     # Subject Enrolment System (enrol, remove, show, change password)
    └── admin_controller.py       # Admin System (show, group, partition, remove, clear)
```

---

## 🚀 Getting Started

### Prerequisites

- Python **3.8+** (no third-party libraries required — uses only the standard library)

### Run the app

```bash
python CLIUniApp.py
```

---

## 🗺️ System Menus

### University System
```
University System: (A)dmin, (S)tudent, or X :
```
| Input | Action |
|-------|--------|
| `A`   | Enter Admin subsystem |
| `S`   | Enter Student subsystem |
| `X`   | Exit application |

---

### Student System
```
        Student System (l/r/x):
```
| Input | Action |
|-------|--------|
| `l`   | Login |
| `r`   | Register |
| `x`   | Exit to University menu |

---

### Subject Enrolment System *(after login)*
```
        Student Course Menu (c/e/r/s/x):
```
| Input | Action |
|-------|--------|
| `c`   | Change password |
| `e`   | Enrol in a subject (max 4) |
| `r`   | Remove a subject by ID |
| `s`   | Show enrolled subjects with marks & grades |
| `x`   | Exit to Student menu |

---

### Admin System
```
        Admin System (c/g/p/r/s/x):
```
| Input | Action |
|-------|--------|
| `c`   | Clear all student data |
| `g`   | Group students by grade |
| `p`   | Partition students into PASS / FAIL |
| `r`   | Remove a student by ID |
| `s`   | Show all students |
| `x`   | Exit to University menu |

---

## ✅ Validation Rules

### Email
- Must follow the pattern: `firstname.lastname@university.com`
- Must contain a dot (`.`) between first and last name
- Must end with `@university.com`

### Password
- Must start with an **uppercase** letter
- Must contain **at least 6 letters** in total (uppercase start + 5 more)
- Must end with **3 or more digits**
- Example: `Helloworld123` ✅ &nbsp;|&nbsp; `Hello123` ❌ &nbsp;|&nbsp; `helloworld123` ❌

---

## 📐 Business Rules

| Rule | Detail |
|------|--------|
| Max subjects | A student can enrol in a maximum of **4 subjects** |
| Subject mark | Randomly generated between **25 and 100** upon enrolment |
| Grades | HD ≥ 85 · D ≥ 75 · C ≥ 65 · P ≥ 50 · F < 50 |
| Pass condition | Student average mark **≥ 50** across all subjects |
| Student ID | Unique, randomly generated **6-digit** number (000001–999999) |
| Subject ID | Unique, randomly generated **3-digit** number (001–999) |
| Data storage | All data persisted in `students.data` using Python `pickle` |
| Admin access | Admins access the system directly — **no registration required** |

---

## 💾 Data Persistence

All student and subject data is stored in `students.data` (binary, pickle format) in the project root.  
The file is created automatically on first run. All CRUD operations read from and write to this file.

---

## 📸 Sample I/O

**Registration:**
```
University System: (A)dmin, (S)tudent, or X : S
        Student System (l/r/x): r
        Student Sign Up
        Email: johnsmith@university.com
        Password: helloworld123
        Incorrect email or password format
        Email: john.smith@university.com
        Password: Helloworld123
        email and password formats acceptable
        Name: John Smith
        Enrolling Student John Smith
        Student System (l/r/x):
```

**Enrolment:**
```
        Student Course Menu (c/e/r/s/x): e
        Enrolling in Subject-541
        You are now enrolled in 1 out of 4 subjects
        Student Course Menu (c/e/r/s/x): s
        Showing 1 subjects
        [ Subject::541 -- mark = 55 -- grade =   P ]
```

**Admin – Group & Partition:**
```
        Admin System (c/g/p/r/s/x): g
        Grade Grouping
        P --> [Alen Jones :: 762740 --> GRADE:  P - MARK: 63.50]
        Admin System (c/g/p/r/s/x): p
        PASS/FAIL Partition
        FAIL --> []
        PASS --> [Alen Jones :: 762740 --> GRADE:  P - MARK: 63.50]
```

