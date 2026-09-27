# tests/test_project.py
# verification test suite using pure Python assert statements
# python essentials project

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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
from main import chk_float


def test_patient():
    print("Testing Patient class...")
    p = Patient(501, "Test User", 30, "Male", "Fever", "General", 101, True, 150.0, S_CON)
    assert p.pid == 501
    assert p.name == "Test User"
    assert p.age == 30
    assert p.gen == "Male"
    assert p.dis == "Fever"
    assert p.dept == "General"
    assert p.room == 101
    assert p.admitted is True
    assert p.chg == 150.0

    p.disch()
    assert p.admitted is False
    assert p.room == 0

    p.admit(202)
    assert p.admitted is True
    assert p.room == 202

    p.edit_p("Cough", "General", 205, 175.0)
    assert p.dis == "Cough"
    assert p.room == 205
    assert p.chg == 175.0
    print(" -> Patient tests passed.")


def test_bitwise():
    print("Testing Bitwise flags...")
    f = S_CON
    assert has_srv(f, S_CON) is True
    assert has_srv(f, S_LAB) is False
    f |= S_LAB
    assert has_srv(f, S_LAB) is True
    f2 = comb_srv(f, S_PHA)
    assert has_srv(f2, S_PHA) is True
    print(" -> Bitwise tests passed.")


def test_hospital():
    print("Testing Hospital class...")
    h = Hospital("Test Hospital")
    assert len(h.pList) == 0
    p1 = Patient(1, "P1", 20, "Male", "Flu", "General", 10, True, 100.0)
    p2 = Patient(2, "P2", 22, "Female", "Cold", "General", 0, False, 50.0)
    assert h.add_p(p1) is True
    assert h.add_p(p2) is True
    assert h.add_p(Patient(1, "Duplicate", 30, "Male", "Headache", "General", 0, False, 20.0)) is False

    assert h.get_p(1) is not None
    assert h.get_p(999) is None

    adms = h.get_adm()
    assert len(adms) == 1
    assert adms[0].pid == 1

    tup = h.p_tuple(1)
    assert tup == (1, "P1", "General", True)

    dis_set = h.all_dis()
    assert "Flu" in dis_set
    assert "Cold" in dis_set

    arr = h.c_arr()
    assert sum(arr) == 150.0

    assert h.del_p(2) is True
    assert h.get_p(2) is None
    print(" -> Hospital tests passed.")


def test_billing():
    print("Testing Bill calculation...")
    tot, a_day, weeks, rem = calc_bill(rate=50.0, days=10, fee=100.0, disc=20.0)
    assert tot == 580.0
    assert a_day == 58.0
    assert weeks == 1
    assert rem == 3
    print(" -> Bill tests passed.")


def test_validator():
    print("Testing Float validator...")
    assert chk_float("123.45") is True
    assert chk_float("100") is True
    assert chk_float("abc") is False
    assert chk_float("12.34.56") is False
    print(" -> Validator tests passed.")


def run_all():
    print("==================================================")
    print("   RUNNING PROJECT TESTS (PLAIN PYTHON ASSERTS)   ")
    print("==================================================")
    test_patient()
    test_bitwise()
    test_hospital()
    test_billing()
    test_validator()
    print("==================================================")
    print("All tests passed successfully!")
    print("==================================================")


if __name__ == "__main__":
    run_all()
