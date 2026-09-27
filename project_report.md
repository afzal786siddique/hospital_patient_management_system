# Academic Project Report: Hospital Patient Management System

**Course**: Python Essentials  
**Academic Level**: First-Year Undergraduate  
**Project Title**: Hospital Patient Management System (CLI Application)  
**Programming Language**: Python 3 (Pure Standard Built-ins)  

---

## 1. Title
**Hospital Patient Management System**  
A Terminal-Based Academic Management Software Developed in Python.

---

## 2. Introduction
In modern healthcare facilities, tracking patient admissions, doctor assignments, room allocations, and patient charges is a fundamental administrative task. This academic project implements a lightweight, terminal-based **Hospital Patient Management System** designed as part of the *Python Essentials* curriculum.

The project demonstrates practical application of introductory computer science topics including modular programming, control structures, basic object-oriented principles, and fundamental data structures (lists, tuples, sets, dictionaries, frozensets, and arrays).

---

## 3. Problem Statement
Many introductory programming assignments focus on abstract mathematical algorithms without connecting them to real-world scenarios. Conversely, large hospital software uses complicated databases, cloud servers, and web frameworks that are far beyond the scope of a first-year student.

The challenge is to design an authentic, functional, and user-friendly hospital management application that:
- Solves genuine record-tracking problems (admissions, room assignments, billing).
- Stays strictly within the boundaries of introductory Python fundamentals.
- Avoids unstudied techniques such as `try/except` exception handling, external packages, and database engines.

---

## 4. Objectives
1. Provide a menu-driven command-line interface for hospital record management.
2. Implement patient registration, search, modification, admission, and discharge workflows.
3. Compute stay invoices using genuine arithmetic operators and operator precedence.
4. Calculate administrative statistics (total counts, unique diseases, active departments, average charges).
5. Apply all 23 core topics taught in the Python Essentials curriculum in a natural, cohesive design.

---

## 5. Technologies and Concepts Used
The project is built entirely with Python 3 built-in capabilities:

- **I/O & Fundamentals**: `input()`, `print()`, variable assignments, comments.
- **Data Types**: `int`, `float`, `str`, `bool`.
- **Operators**:
  - Arithmetic: `+`, `-`, `*`, `/`, `//`, `%`.
  - Assignment: `=`, `+=`, `-=`, `|=`.
  - Relational: `==`, `!=`, `<`, `>`, `<=`, `>=`.
  - Logical: `and`, `or`, `not`.
  - Membership: `in`, `not in`.
  - Identity: `is`, `is not` (applied to `None` lookups).
  - Bitwise: `|`, `&` (for binary medical service flags).
- **Control Flow**: `while` loops for validation and menu looping, `for` loops for data iteration, `if/elif/else` branching, `break`, `continue`.
- **Object-Oriented Programming**: `class`, `__init__` constructor, instance variables, instance methods.
- **Built-in Data Collections**: Lists, Tuples, Sets, Dictionaries, Frozensets, and standard `array.array`.
- **Verification**: Python `assert` statements.

---

## 6. System Features

1. **Patient Registration**: Enrolls patients with unique ID, name, age, gender, disease, department, room, and fees.
2. **Patient Directory**: Displays all registered patients and automatically looks up their department head doctor.
3. **Record Search**: Instant lookup by Patient ID; reports whether a patient exists or not.
4. **Information Update**: Allows editing disease diagnosis, department transfer, and fee adjustments.
5. **Patient Deletion**: Permanently removes a record after manual user confirmation.
6. **Room Admission**: Assigns an admitted patient to a specified room number.
7. **Patient Discharge**: Marks an admitted patient as discharged and frees up their room.
8. **Admitted Patients Listing**: Displays a clean, tabular view of only currently hospitalized patients.
9. **Patient Billing**: Computes hospital bills including daily room rates, duration, consultation fees, and discounts.
10. **Hospital Statistics**: Analyzes patient records to compute active departments, unique diseases, total revenue, and average charge per patient.
11. **Application Exit**: Exits the program cleanly.

---

## 7. Data Structures Used

| Data Structure | Code Location | Practical Purpose |
| :--- | :--- | :--- |
| **List (`list`)** | `Hospital.patients` | Stores all active `Patient` objects. Allows dynamic appending, iterating, and removing. |
| **Tuple (`tuple`)** | `GENDER_OPTIONS`<br>`Hospital.get_patient_summary()` | Holds fixed choices (`"Male"`, `"Female"`, `"Other"`) and packages immutable record summaries `(id, name, dept, status)`. |
| **Set (`set`)** | `Hospital.get_unique_diseases()`<br>`Hospital.get_unique_departments()` | Leverages automatic deduplication to identify unique medical conditions treated and unique active departments. |
| **Dictionary (`dict`)** | `DEPT_DOCTORS` | Maps department names (`"Cardiology"`) to corresponding attending physicians (`"Dr. Sarah Adams"`). |
| **Frozenset (`frozenset`)** | `VALID_DEPARTMENTS`<br>`ROOM_CATEGORIES` | Represents strict, immutable hospital rules (departments and room types) that cannot be altered at runtime. |
| **Array (`array.array`)** | `Hospital.get_charges_array()` | Uses typecode `'d'` (double float) to store numeric fees for statistical summation and averages. |

---

## 8. Functions Used

### Helper and Validation Functions (`main.py`):
- `is_valid_float_string(text)`: Inspects characters in a string to verify valid decimal format without `try/except`.
- `input_positive_int(prompt)`: Loops until whole non-negative digits are supplied.
- `input_positive_float(prompt)`: Prompts and validates floating-point currency numbers.
- `input_gender()`: Validates choice against `GENDER_OPTIONS` using `in`.
- `input_department()`: Validates input against `VALID_DEPARTMENTS` using `in`.
- `populate_sample_patients(hospital)`: Initializes 3 realistic patient profiles on launch.
- `display_menu()`: Renders the 11-option terminal menu.

### Billing Functions (`billing.py`):
- `calculate_bill(daily_rate, days_admitted, consultation_fee, discount)`: Computes final invoice, daily average, weeks, and remaining days.
- `combine_service_flags(flag_a, flag_b)`: Combines service bitmasks using `|`.
- `has_service(service_flags, query_flag)`: Checks active service bits using `&`.
- `get_service_descriptions(service_flags)`: Translates bitmask integers into readable text descriptions.

---

## 9. OOP Implementation

The system utilizes two primary classes without unnecessary magic methods:

### 1. `Patient` Class (`patient.py`)
- **Constructor (`__init__`)**: Initializes 10 instance variables (`patient_id`, `name`, `age`, `gender`, `disease`, `department`, `room_number`, `is_admitted`, `basic_charges`, `service_flags`).
- **Methods**:
  - `display_info()`: Outputs patient attributes in a standardized visual card.
  - `admit(room_number)`: Updates admission status and assigns room.
  - `discharge()`: Clears admission status and resets room to 0.
  - `update_details(disease, dept, room, charges)`: Updates patient record fields.
  - `add_service(service_flag)`: Appends an extra service flag using `|=`.
  - `has_service(service_flag)`: Checks if a service flag is enabled using `&`.

### 2. `Hospital` Class (`hospital.py`)
- **Constructor (`__init__`)**: Initializes `self.hospital_name` and an empty list `self.patients = []`.
- **Methods**:
  - `add_patient(patient)`: Appends patient after verifying no duplicate ID exists.
  - `get_patient_by_id(patient_id)`: Searches and returns the matching object or `None`.
  - `remove_patient(patient_id)`: Removes patient from the list.
  - `get_all_patients()`: Returns the full patient list.
  - `get_admitted_patients()`: Returns filtered list of admitted patients.
  - `get_unique_diseases()`: Returns a `set` of distinct diseases.
  - `get_unique_departments()`: Returns a `set` of distinct departments.
  - `get_charges_array()`: Returns an `array.array('d')` of all charges.
  - `get_patient_summary(patient_id)`: Returns an immutable `tuple`.

---

## 10. Module Structure

The project code is separated into 4 distinct Python modules:

1. `main.py`: Coordinates program flow, handles terminal menus, and contains user input validators.
2. `patient.py`: Defines the `Patient` entity class.
3. `hospital.py`: Defines the `Hospital` management class.
4. `billing.py`: Contains billing logic, immutable constants, and bitwise helper functions.

Automated verification is placed in `tests/test_project.py` using standard `assert` statements.

---

## 11. Sample Input and Output

### Sample 1: Calculating a Bill
```text
--- CALCULATE PATIENT BILL ---
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

### Sample 2: Hospital Statistics
```text
--- HOSPITAL GENERAL STATISTICS ---
Hospital Name             : City General Healthcare
Total Registered Patients : 3
Currently Admitted        : 2
Outpatients / Discharged  : 1

Unique Diagnosed Diseases (3 total - via Set):
  * Arrhythmia
  * Fracture
  * Migraine

Active Departments (3 total - via Set):
  * Cardiology (Head: Dr. Sarah Adams)
  * Neurology (Head: Dr. Robert Chen)
  * Orthopedics (Head: Dr. Michael Brown)

Billing & Revenue Summary (via array.array):
Total Basic Charges Sum   : $1250.00
Average Charge per Patient: $416.67
```

---

## 12. Limitations

1. **Transient Memory**: Records exist in memory only during the active session. When the program exits, data is reset to the initial sample state.
2. **Console-Based Interaction**: Designed specifically for terminal input and output rather than graphical windows.
3. **Single-User Scope**: Intended for academic single-user simulation.

---

## 13. Conclusion
The **Hospital Patient Management System** fulfills all requirements of a beginner academic software project. By adhering strictly to the *Python Essentials* syllabus, it avoids unnecessary frameworks and exception-handling code while demonstrating clean programming style, robust input validation, and genuine usage of all course data structures and operators.
