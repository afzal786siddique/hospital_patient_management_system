# Hospital Patient Management System

A beginner-friendly, terminal-based Python application developed as an academic project for a first-year **Python Essentials** course. This system provides core hospital operations—such as patient registration, record lookups, room admissions and discharges, billing calculations, and hospital-wide statistics—using only fundamental Python concepts.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Python Version Requirement](#python-version-requirement)
5. [Project Structure](#project-structure)
6. [Installation and Setup](#installation-and-setup)
7. [How to Run the Project](#how-to-run-the-project)
8. [Running Automated Tests](#running-automated-tests)
9. [Example Usage](#example-usage)
10. [Course Concepts Demonstrated](#course-concepts-demonstrated)
11. [Limitations](#limitations)
12. [Future Improvements](#future-improvements)

---

## Project Description

The **Hospital Patient Management System** is designed to demonstrate mastery of essential Python programming fundamentals without relying on external libraries, frameworks, or databases. The application manages in-memory patient data structures, models real-world hospital entities through basic Object-Oriented Programming (OOP), and provides an interactive command-line interface.

It strictly adheres to an introductory curriculum:
- **No external packages** (No Pandas, NumPy, etc.)
- **No database engines** (No SQLite, MySQL, etc.)
- **No GUI or web frameworks** (No Tkinter, Flask, Django)
- **No advanced or unstudied language features** (No decorators, generators, multithreading, or `try/except` statements)

---

## Features

The system offers 11 core terminal options:

1. **Add Patient**: Register a new patient with unique ID, full name, age, gender, disease condition, assigned department, admission status, room number, initial basic charges, and extra service flags.
2. **View Patients**: List all registered patients with clear formatting and their attending head doctors.
3. **Search Patient**: Look up a patient by numeric ID, displaying full records and summary tuples.
4. **Update Patient**: Modify disease diagnosis, department assignment, and basic charges for existing patients.
5. **Delete Patient**: Safely remove a patient record from hospital records after confirmation.
6. **Admit Patient**: Assign a hospital bed/room and update the admission status to `Admitted`.
7. **Discharge Patient**: Discharge an admitted patient and automatically release their room back to the hospital.
8. **View Admitted Patients**: Filter and display a focused tabular view of currently hospitalized patients.
9. **Calculate Bill**: Compute a comprehensive patient bill based on daily bed rates, stay duration, doctor consultation fees, and discounts, displaying both total and daily averages.
10. **Hospital Statistics**: Display overall administrative summaries, including total patient count, admitted counts, unique diseases diagnosed (via Sets), active departments, and total revenue analysis (via the standard `array` module).
11. **Exit**: Gracefully terminate the interactive terminal loop.

---

## Technologies Used

- **Language**: Python 3 (Standard Library only)
- **Built-in Modules**: `array`, `sys`, `os`
- **Data Structures**: Lists, Tuples, Sets, Dictionaries, Frozensets, Numerical Arrays (`array.array`)
- **Testing**: Pure Python `assert` assertions

---

## Python Version Requirement

- **Python 3.8+** (Tested on Python 3.8, 3.10, 3.11, and 3.12)
- Zero external dependencies required.

---

## Project Structure

```text
hospital_patient_management/
│
├── main.py                  # Main terminal loop, user interface, and non-exception validators
├── patient.py               # Patient class definition (attributes, constructor, instance methods)
├── hospital.py              # Hospital class managing patient lists, searches, sets, and arrays
├── billing.py               # Bill computation, bitwise service flags, and immutable constants
├── tests/
│   └── test_project.py      # Automated verification test suite using pure Python assert statements
├── README.md                # Project documentation and user manual
└── project_report.md        # Academic report written at a first-year student level
```

---

## Installation and Setup

1. **Clone or Download** the project files to your local computer.
2. Open your terminal / command prompt.
3. Navigate to the project root directory:
   ```bash
   cd hospital_patient_management
   ```

No virtual environment or `pip install` commands are needed because the project uses 100% standard built-in Python.

---

## How to Run the Project

Run the application directly using standard Python:

```bash
python main.py
```

*(On Linux or macOS, use `python3 main.py` if `python` defaults to Python 2).*

---

## Running Automated Tests

The project includes an automated test script that tests all classes, data structures, and billing formulas using plain Python `assert` statements:

```bash
python tests/test_project.py
```

Expected output:
```text
==================================================
   RUNNING PROJECT TESTS (PLAIN PYTHON ASSERTS)   
==================================================
Testing Patient creation and instance methods...
 -> Patient tests passed.
Testing bitwise operations for medical service flags...
 -> Bitwise service flag tests passed.
Testing Hospital class operations, list handling, and identity checks...
 -> Hospital management tests passed.
Testing sets, frozensets, tuples, dictionaries, and array data structure...
 -> Data structure tests passed.
Testing billing calculations, operator precedence, and mixed division...
 -> Billing and operator tests passed.
==================================================
All tests passed successfully!
==================================================
```

---

## Example Usage

### 1. Startup and Main Menu
When launched, sample patients (`101`, `102`, and `103`) are automatically pre-loaded so you can immediately explore features without manual data entry.

```text
==========================================
    HOSPITAL PATIENT MANAGEMENT SYSTEM    
==========================================
1.  Add Patient
2.  View Patients
3.  Search Patient
4.  Update Patient
5.  Delete Patient
6.  Admit Patient
7.  Discharge Patient
8.  View Admitted Patients
9.  Calculate Bill
10. Hospital Statistics
11. Exit
==========================================
Enter your choice (1-11): 
```

### 2. Searching for a Patient (Option 3)
```text
Enter Patient ID to search: 101

Patient Record Found:
---------------------------------------------
Patient ID        : 101
Name              : Alice Johnson
Age               : 32
Gender            : Female
Disease / Condition: Arrhythmia
Department        : Cardiology
Admission Status  : Admitted
Room Number       : 201
Basic Charges     : $450.00
Services Availed  : Doctor Consultation, Laboratory Tests
---------------------------------------------
Attending Doctor  : Dr. Sarah Adams
Record Tuple Summary: (101, 'Alice Johnson', 'Cardiology', True)
```

### 3. Calculating a Hospital Bill (Option 9)
```text
Enter Patient ID for billing: 101
Generating bill for: Alice Johnson (ID: 101)
Base Registered Charges: $450.00
Enter number of days admitted / treated: 5
Enter room/bed daily rate ($): 150.00
Enter doctor consultation fee ($): 50.00
Enter any applicable discount ($): 25.00

================== HOSPITAL INVOICE ==================
Patient Name         : Alice Johnson
Patient ID           : 101
Stay Duration        : 5 day(s) (0 full week(s) and 5 day(s))
Doctor Consultation  : $50.00
Room Charges (5 x $150.00): $750.00
Discount Applied     : -$25.00
Stay Subtotal        : $775.00
Average Cost / Day   : $155.00
Base Medical Charges : $450.00
------------------------------------------------------
FINAL PAYABLE AMOUNT : $1225.00
======================================================
```

---

## Course Concepts Demonstrated

Every concept from the Python Essentials syllabus is integrated with educational purpose:

1. **Python Fundamentals**: Clean script execution, descriptive variable names, and clear comments.
2. **Input and Output Operations**: User input collection via `input()` and clean CLI formatting via `print()`.
3. **Arithmetic Operators (`+`, `-`, `*`, `/`, `//`, `%`)**:
   - `*`, `+`, `-`: Computing bill totals.
   - `/`: Calculating average cost per day and average hospital charges.
   - `//` and `%`: Breaking stay durations into weeks (`days // 7`) and remaining days (`days % 7`).
4. **Assignment Operators (`=`, `+=`, `-=`, `|=`)**: Used for accumulators and bitwise flag assignments.
5. **Relational Operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)**: ID matching, valid ranges (`0 <= age <= 125`), and positive charge validations.
6. **Logical Operators (`and`, `or`, `not`)**: Multi-condition branching (e.g. `if not text:`, `if is_admitted and room_number > 0:`).
7. **Membership Operators (`in`, `not in`)**: Checking choices against tuples (`choice in GENDER_OPTIONS`) and frozensets (`dept in VALID_DEPARTMENTS`).
8. **Identity Operators (`is`, `is not`)**: Checking search results against `None` (`if patient is None:` and `if patient is not None:`).
9. **Bitwise Operators (`&`, `|`)**: Managing binary service flags (Consultation = 1, Lab = 2, Pharmacy = 4) using `|` to combine and `&` to query active services.
10. **Type Function (`type()`)**: Inspected in the Hospital Statistics module to verify underlying types (`type(total_count)`, `type(charges_array)`).
11. **Type Conversion (`int()`, `float()`, `str()`)**: Converting validated numeric strings into proper arithmetic types.
12. **Division with Mixed Data Types**: Dividing floating-point revenue by integer patient count producing a standard float.
13. **Operator Precedence**: Demonstrated in bill calculations where multiplication (`daily_rate * days`) takes precedence over addition and subtraction.
14. **Lists**: `hospital.patients = []` storing the collection of patient instances.
15. **Tuples**: `GENDER_OPTIONS = ("Male", "Female", "Other")` and fixed summary records `(id, name, dept, status)`.
16. **Sets**: Deduplicating diagnosed conditions (`hospital.get_unique_diseases()`) and active departments.
17. **Dictionaries**: Key-value lookup for attending department doctors (`DEPT_DOCTORS`).
18. **Frozen Sets**: Fixed hospital configurations (`VALID_DEPARTMENTS = frozenset(...)`, `ROOM_CATEGORIES = frozenset(...)`).
19. **Control Flow**: `while` loops for input loops and menus, `for` loops for data iteration, `if/elif/else` branching, `break`, and `continue`.
20. **Functions**: Modular, reusable helper routines with parameters and return values.
21. **Modules**: Separated concerns across `main.py`, `patient.py`, `hospital.py`, and `billing.py`.
22. **Array Data Structure**: The standard `array.array('d')` holding homogeneous numerical charges for financial analysis.
23. **Object-Oriented Programming (OOP)**: `Patient` and `Hospital` classes featuring constructors (`__init__`), instance variables, and instance methods.

---

## Limitations

- **In-Memory Storage**: Patient records reset when the application exits because file persistence and databases are outside the course syllabus.
- **Single Terminal Session**: Designed for one administrative user at a time in a local command-line environment.
- **Manual Date Entry**: Days admitted are recorded as whole integer values rather than importing Python's `datetime` module.

---

## Future Improvements

- Add persistent storage using basic text/CSV files once file I/O is covered in future units.
- Implement appointment scheduling and doctor time slots.
- Introduce advanced report generation and bill receipt printing.
