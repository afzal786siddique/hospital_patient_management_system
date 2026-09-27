# billing.py
# module for billing calculations and service constants
# python essentials project

# bitwise flags for medical services
S_CON = 1   # binary: 001
S_LAB = 2   # binary: 010
S_PHA = 4   # binary: 100

# tuple for fixed gender choices
GENDERS = ("Male", "Female", "Other")

# frozenset for valid hospital departments
DEPTS = frozenset([
    "Cardiology",
    "Neurology",
    "Pediatrics",
    "General",
    "Orthopedics"
])

# frozenset for hospital room categories
ROOMS = frozenset([
    "General",
    "Semi-Private",
    "Private",
    "ICU"
])

# dictionary of attending department doctors
DOCTORS = {
    "Cardiology": "Dr. Sarah Adams",
    "Neurology": "Dr. Robert Chen",
    "Pediatrics": "Dr. Emily Taylor",
    "General": "Dr. James Wilson",
    "Orthopedics": "Dr. Michael Brown"
}

# function to calculate hospital bill
def calc_bill(rate, days, fee, disc):
    # multiplication has higher precedence than addition and subtraction
    tot = fee + (rate * days) - disc
    if tot < 0.0:
        tot = 0.0

    # mixed type division: float total divided by int days
    if days > 0:
        a_day = tot / days
    else:
        a_day = 0.0

    # floor division for whole weeks
    weeks = days // 7
    # modulo for remaining days
    rem = days % 7

    return tot, a_day, weeks, rem

# combine service flags with bitwise OR
def comb_srv(f1, f2):
    return f1 | f2

# check service flag with bitwise AND
def has_srv(flags, srv):
    if (flags & srv) != 0:
        return True
    else:
        return False

# get list of services from bitwise flags
def srv_list(flags):
    s_arr = []
    if has_srv(flags, S_CON) == True:
        s_arr.append("Doctor Consultation")
    if has_srv(flags, S_LAB) == True:
        s_arr.append("Laboratory Tests")
    if has_srv(flags, S_PHA) == True:
        s_arr.append("Pharmacy Medications")

    if len(s_arr) == 0:
        s_arr.append("No Extra Services")

    return s_arr
