# hospital.py
# hospital management class
# python essentials project

import array
from patient import Patient


# hospital class to manage patient records
class Hospital:
    # constructor
    def __init__(self, hname):
        self.hname = hname
        # list data structure to hold patient objects
        self.pList = []

    # add patient after checking for duplicate id
    def add_p(self, p):
        # loop by index to verify id uniqueness
        for i in range(len(self.pList)):
            if self.pList[i].pid == p.pid:
                return False
        self.pList.append(p)
        return True

    # search patient by id
    def get_p(self, pid):
        # loop by index
        for i in range(len(self.pList)):
            if self.pList[i].pid == pid:
                return self.pList[i]
        return None

    # remove patient from list
    def del_p(self, pid):
        p = self.get_p(pid)
        # identity check with is not None
        if p is not None:
            self.pList.remove(p)
            return True
        return False

    # return full patients list
    def all_p(self):
        return self.pList

    # return list of admitted patients
    def get_adm(self):
        adms = []
        for i in range(len(self.pList)):
            p = self.pList[i]
            if p.admitted == True:
                adms.append(p)
        return adms

    # get set of unique diseases
    def all_dis(self):
        d_set = set()
        for i in range(len(self.pList)):
            d_set.add(self.pList[i].dis)
        return d_set

    # get set of unique departments
    def all_depts(self):
        d_set2 = set()
        for i in range(len(self.pList)):
            d_set2.add(self.pList[i].dept)
        return d_set2

    # get array of charges
    def c_arr(self):
        # array module with typecode d for double float
        c_arr = array.array('d', [])
        for i in range(len(self.pList)):
            c_arr.append(self.pList[i].chg)
        return c_arr

    # get tuple summary
    def p_tuple(self, pid):
        p = self.get_p(pid)
        if p is not None:
            # tuple with fixed info
            return (p.pid, p.name, p.dept, p.admitted)
        return None
