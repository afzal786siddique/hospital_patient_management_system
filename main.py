# main.py
# main entry point for the hospital patient management system
# python essentials project

import sys
from patient import Patient
from hospital import Hospital
from billing import (
    calc_bill,
    comb_srv,
    has_srv,
    S_CON,
    S_LAB,
    S_PHA,
    GENDERS,
    DEPTS,
    ROOMS,
    DOCTORS
)


# check if string is valid float without try-except
def chk_float(txt):
    if len(txt) == 0:
        return False
    if txt[0] == "+":
        txt = txt[1:]
    if len(txt) == 0:
        return False

    dots = 0
    digits = 0
    for i in range(len(txt)):
        c = txt[i]
        if c == ".":
            dots = dots + 1
        elif c.isdigit() == True:
            digits = digits + 1
        else:
            return False

    if dots <= 1 and digits > 0:
        return True
    else:
        return False


# read positive integer
def get_int(msg):
    while True:
        val = input(msg).strip()
        if val.isdigit() == True:
            num = int(val)
            if num >= 0:
                return num
            else:
                print("Error: Number must be positive or 0.")
        else:
            print("Error: Please enter digits only.")


# read positive float
def get_float(msg):
    while True:
        val = input(msg).strip()
        if chk_float(val) == True:
            return float(val)
        else:
            print("Error: Invalid decimal number. Try again.")


# read gender from tuple
def get_gender():
    while True:
        print("Allowed Genders: " + ", ".join(GENDERS))
        g = input("Enter gender: ").strip().capitalize()
        # membership check with in operator
        if g in GENDERS:
            return g
        print("Error: Invalid gender choice.")


# read department from frozenset
def get_dept():
    d_arr = list(DEPTS)
    while True:
        print("Available Departments:")
        for i in range(len(d_arr)):
            dname = d_arr[i]
            d_doc = DOCTORS.get(dname, "No Doctor")
            print(" - " + dname + " (Head: " + d_doc + ")")
        choice = input("Enter department name: ").strip().capitalize()
        # membership check with in operator
        if choice in DEPTS:
            return choice
        print("Error: Invalid department choice.")


# load sample patient records
def init_p(h):
    f1 = S_CON | S_LAB
    p1 = Patient(101, "Alice Johnson", 32, "Female", "Arrhythmia", "Cardiology", 201, True, 450.0, f1)

    f2 = S_CON | S_PHA
    p2 = Patient(102, "Bob Williams", 45, "Male", "Migraine", "Neurology", 0, False, 180.0, f2)

    f3 = comb_srv(S_CON | S_LAB, S_PHA)
    p3 = Patient(103, "Clara Davis", 8, "Female", "Fracture", "Orthopedics", 305, True, 620.0, f3)

    h.add_p(p1)
    h.add_p(p2)
    h.add_p(p3)


# 1. add patient
def opt_add(h):
    print("\n--- ADD PATIENT ---")
    while True:
        pid = get_int("Enter new Patient ID: ")
        # identity check with is not None
        p_old = h.get_p(pid)
        if p_old is not None:
            print("Error: ID already exists. Enter a unique ID.")
        else:
            break

    while True:
        name = input("Enter Patient Name: ").strip()
        if len(name) > 0:
            break
        print("Error: Name cannot be empty.")

    while True:
        age = get_int("Enter Patient Age: ")
        if age >= 0 and age <= 125:
            break
        print("Error: Age must be between 0 and 125.")

    gen = get_gender()

    while True:
        dis = input("Enter Disease / Diagnosis: ").strip()
        if len(dis) > 0:
            break
        print("Error: Disease cannot be empty.")

    dept = get_dept()

    ans = input("Is patient admitted? (yes/no): ").strip().lower()
    if ans == "yes" or ans == "y":
        adm = True
        room = get_int("Enter Room Number: ")
        while room <= 0:
            print("Room number must be greater than 0.")
            room = get_int("Enter Room Number: ")
    else:
        adm = False
        room = 0

    chg = get_float("Enter Initial Charges ($): ")

    # bitwise service flags
    flags = S_CON
    print("\nExtra Services (Bitwise Flags):")
    a1 = input("Include Lab Tests? (yes/no): ").strip().lower()
    if a1 == "yes" or a1 == "y":
        flags |= S_LAB

    a2 = input("Include Pharmacy? (yes/no): ").strip().lower()
    if a2 == "yes" or a2 == "y":
        flags |= S_PHA

    new_p = Patient(pid, name, age, gen, dis, dept, room, adm, chg, flags)
    ok = h.add_p(new_p)
    if ok == True:
        print("\nSuccess: Patient " + name + " (ID: " + str(pid) + ") registered!")
    else:
        print("\nError: Could not add patient.")


# 2. view all patients
def opt_view(h):
    print("\n--- ALL PATIENTS ---")
    plist = h.all_p()
    if len(plist) == 0:
        print("No patients in the system.")
        return

    print("Total Patients: " + str(len(plist)))
    for i in range(len(plist)):
        p = plist[i]
        p.show()
        doc = DOCTORS.get(p.dept, "N/A")
        print("Attending Doctor  : " + doc)


# 3. search patient
def opt_find(h):
    print("\n--- SEARCH PATIENT ---")
    pid = get_int("Enter Patient ID to search: ")
    p = h.get_p(pid)

    # identity check with is None
    if p is None:
        print("Search Result: Patient ID " + str(pid) + " not found.")
    elif p is not None:
        print("\nPatient Found:")
        p.show()
        doc = DOCTORS.get(p.dept, "N/A")
        print("Attending Doctor  : " + doc)
        tup = h.p_tuple(pid)
        print("Summary Tuple     : " + str(tup))


# 4. edit_p patient
def opt_edit(h):
    print("\n--- UPDATE PATIENT ---")
    pid = get_int("Enter Patient ID to edit_p: ")
    p = h.get_p(pid)

    if p is None:
        print("Error: Patient ID " + str(pid) + " not found.")
        return

    print("\nCurrent Details:")
    p.show()

    n_dis = input("Enter new disease [" + p.dis + "]: ").strip()
    if len(n_dis) == 0:
        n_dis = p.dis

    ans = input("Change department? (yes/no): ").strip().lower()
    if ans == "yes" or ans == "y":
        n_dept = get_dept()
    else:
        n_dept = p.dept

    n_chg = get_float("Enter updated charges [Current: $%.2f]: " % p.chg)
    p.edit_p(n_dis, n_dept, p.room, n_chg)
    print("\nSuccess: Patient ID " + str(pid) + " updated successfully!")


# 5. delete patient
def opt_del(h):
    print("\n--- DELETE PATIENT ---")
    pid = get_int("Enter Patient ID to delete: ")
    p = h.get_p(pid)

    if p is None:
        print("Error: Patient ID " + str(pid) + " not found.")
        return

    ans = input("Are you sure you want to delete " + p.name + "? (yes/no): ").strip().lower()
    if ans == "yes" or ans == "y":
        ok = h.del_p(pid)
        if ok == True:
            print("Success: Patient removed.")
        else:
            print("Error: Could not remove.")
    else:
        print("Deletion cancelled.")


# 6. admit patient
def opt_admit(h):
    print("\n--- ADMIT PATIENT ---")
    pid = get_int("Enter Patient ID to admit: ")
    p = h.get_p(pid)

    if p is None:
        print("Error: Patient ID " + str(pid) + " not found.")
        return

    if p.admitted == True:
        print("Notice: Patient already admitted in room " + str(p.room) + ".")
        return

    room = get_int("Enter Room Number to assign: ")
    while room <= 0:
        print("Room number must be greater than 0.")
        room = get_int("Enter Room Number to assign: ")

    p.admit(room)
    print("Success: Patient " + p.name + " admitted to room " + str(room) + ".")


# 7. disch patient
def opt_out(h):
    print("\n--- DISCHARGE PATIENT ---")
    pid = get_int("Enter Patient ID to disch: ")
    p = h.get_p(pid)

    if p is None:
        print("Error: Patient ID " + str(pid) + " not found.")
        return

    if p.admitted == False:
        print("Notice: Patient is not currently admitted.")
        return

    o_room = p.room
    p.disch()
    print("Success: Patient discharged. Room " + str(o_room) + " is now free.")


# 8. view admitted patients
def opt_adms(h):
    print("\n--- ADMITTED PATIENTS ---")
    adms = h.get_adm()

    if len(adms) == 0:
        print("No admitted patients right now.")
        return

    print("Total Admitted: " + str(len(adms)) + "\n")
    print("%-8s %-20s %-15s %-8s %-12s" % ("ID", "Name", "Department", "Room", "Charges ($)"))
    print("-" * 65)
    for i in range(len(adms)):
        p = adms[i]
        print("%-8d %-20s %-15s %-8d %-12.2f" % (p.pid, p.name, p.dept, p.room, p.chg))
    print("-" * 65)


# 9. calculate bill
def opt_bill(h):
    print("\n--- CALCULATE BILL ---")
    pid = get_int("Enter Patient ID: ")
    p = h.get_p(pid)

    if p is None:
        print("Error: Patient ID " + str(pid) + " not found.")
        return

    print("Patient: " + p.name + " (ID: " + str(p.pid) + ")")
    print("Base Charges: $%.2f" % p.chg)

    days = get_int("Enter days admitted / treated: ")
    rate = get_float("Enter daily bed rate ($): ")
    fee = get_float("Enter consultation fee ($): ")
    disc = get_float("Enter discount amount ($): ")

    tot, a_day, weeks, rem = calc_bill(rate, days, fee, disc)
    fin_tot = p.chg + tot

    print("\n================== HOSPITAL INVOICE ==================")
    print("Patient Name         : " + p.name)
    print("Patient ID           : " + str(p.pid))
    print("Stay Duration        : %d day(s) (%d weeks and %d days)" % (days, weeks, rem))
    print("Doctor Consultation  : $%.2f" % fee)
    print("Room Charges         : $%.2f" % (rate * days))
    print("Discount Applied     : -$%.2f" % disc)
    print("Stay Subtotal        : $%.2f" % tot)
    print("Average Cost / Day   : $%.2f" % a_day)
    print("Base Medical Charges : $%.2f" % p.chg)
    print("------------------------------------------------------")
    print("FINAL PAYABLE AMOUNT : $%.2f" % fin_tot)
    print("======================================================")


# 10. hospital statistics
def opt_stats(h):
    print("\n--- HOSPITAL STATISTICS ---")
    plist = h.all_p()
    tot = len(plist)

    if tot == 0:
        print("No patient records.")
        return

    adms = h.get_adm()
    a_cnt = len(adms)
    o_cnt = tot - a_cnt

    d_set = h.all_dis()
    d_set2 = h.all_depts()
    c_arr = h.c_arr()

    rev = 0.0
    for i in range(len(c_arr)):
        rev = rev + c_arr[i]

    # mixed type division: float divided by int
    a_chg = rev / tot

    print("Hospital Name             : " + h.hname)
    print("Total Registered Patients : " + str(tot))
    print("Currently Admitted        : " + str(a_cnt))
    print("Outpatients / Discharged  : " + str(o_cnt))

    print("\nUnique Diagnosed Diseases (" + str(len(d_set)) + " total via Set):")
    d_arr = list(d_set)
    for i in range(len(d_arr)):
        print("  * " + d_arr[i])

    print("\nActive Departments (" + str(len(d_set2)) + " total via Set):")
    depts = list(d_set2)
    for i in range(len(depts)):
        dname = depts[i]
        doc = DOCTORS.get(dname, "N/A")
        print("  * " + dname + " (Head: " + doc + ")")

    print("\nBilling Summary (via array.array):")
    print("Total Charges Sum         : $%.2f" % rev)
    print("Average Charge per Patient: $%.2f" % a_chg)

    # display types for course syllabus
    print("\n[Educational Inspection of Course Data Types]")
    print("type(tot)         : " + str(type(tot)))
    print("type(rev)         : " + str(type(rev)))
    print("type(d_set)       : " + str(type(d_set)))
    print("type(c_arr)       : " + str(type(c_arr)))
    print("type(GENDERS)     : " + str(type(GENDERS)))
    print("type(DEPTS)       : " + str(type(DEPTS)))


# display menu
def menu():
    print("\n" + "=" * 42)
    print("    HOSPITAL PATIENT MANAGEMENT SYSTEM    ")
    print("=" * 42)
    print("1.  Add Patient")
    print("2.  View Patients")
    print("3.  Search Patient")
    print("4.  Update Patient")
    print("5.  Delete Patient")
    print("6.  Admit Patient")
    print("7.  Discharge Patient")
    print("8.  View Admitted Patients")
    print("9.  Calculate Bill")
    print("10. Hospital Statistics")
    print("11. Exit")
    print("=" * 42)


# main function
def main():
    h = Hospital("City General Healthcare")
    init_p(h)

    print("Welcome to City General Healthcare Patient Management System.")
    print("Sample patient data has been initialized.")

    # menu loop
    while True:
        menu()
        ch_str = input("Enter choice (1-11): ").strip()

        if ch_str.isdigit() == False:
            print("Invalid input! Please enter a number from 1 to 11.")
            continue

        ch = int(ch_str)

        if ch == 1:
            opt_add(h)
        elif ch == 2:
            opt_view(h)
        elif ch == 3:
            opt_find(h)
        elif ch == 4:
            opt_edit(h)
        elif ch == 5:
            opt_del(h)
        elif ch == 6:
            opt_admit(h)
        elif ch == 7:
            opt_out(h)
        elif ch == 8:
            opt_adms(h)
        elif ch == 9:
            opt_bill(h)
        elif ch == 10:
            opt_stats(h)
        elif ch == 11:
            print("\nThank you for using Hospital Patient Management System. Goodbye!")
            break
        else:
            print("Choice out of range! Enter a number between 1 and 11.")


# start program
if __name__ == "__main__":
    main()
