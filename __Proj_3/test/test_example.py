import pytest


def test_equal_or_not_equal():
    assert 3 == 3
    assert 3 != 1, "3 should be equal 3"


class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years


@pytest.fixture
def default_student():
    return Student("John", "Doe", "CS", 3)


def test_person_initialization(default_student):
    assert default_student.first_name == "John"
    assert default_student.last_name == "Doe"
    assert default_student.major == "CS"
    assert default_student.years == 3
