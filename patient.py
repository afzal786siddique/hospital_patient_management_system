# patient.py
# patient class definition
# python essentials project

from billing import has_srv, srv_list, S_CON


# patient class to store individual patient record
class Patient:
    # constructor to initialize 10 patient attributes
    def __init__(self, pid, name, age, gen, dis, dept, room, admitted, chg, flags=0):
        self.pid = pid
        self.name = name
        self.age = age
        self.gen = gen
        self.dis = dis
        self.dept = dept
        self.room = room
        self.admitted = admitted
        self.chg = chg
        self.flags = flags

    # print patient details card
    def show(self):
        # standard if-else check for admission status
        if self.admitted == True:
            st = "Admitted"
            rm = str(self.room)
        else:
            st = "Discharged / Outpatient"
            rm = "Not Assigned"

        s_arr = srv_list(self.flags)
        s_str = ", ".join(s_arr)

        print("---------------------------------------------")
        print("Patient ID        : " + str(self.pid))
        print("Name              : " + self.name)
        print("Age               : " + str(self.age))
        print("Gender            : " + self.gen)
        print("Disease           : " + self.dis)
        print("Department        : " + self.dept)
        print("Admission Status  : " + st)
        print("Room Number       : " + rm)
        print("Basic Charges     : $%.2f" % self.chg)
        print("Services Availed  : " + s_str)
        print("---------------------------------------------")

    # admit patient to room
    def admit(self, rm_no):
        self.admitted = True
        self.room = rm_no

    # disch patient and free room
    def disch(self):
        self.admitted = False
        self.room = 0

    # edit_p patient details
    def edit_p(self, dis, dept, rm_no, n_chg):
        self.dis = dis
        self.dept = dept
        self.room = rm_no
        self.chg = n_chg
        if rm_no > 0:
            self.admitted = True
        else:
            self.admitted = False

    # add extra service flag
    def add_srv(self, srv):
        self.flags |= srv

    # check if patient has specific service
    def chk_srv(self, srv):
        return has_srv(self.flags, srv)
