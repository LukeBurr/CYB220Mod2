# test_employee.py

from employee import Employee

def test_give_default_raise():
    """Test give_raise() method with default raise amount."""
    emp = Employee("John", "Doe", 50000)
    emp.give_raise()
    assert emp.annual_salary == 55000

def test_give_custom_raise():
    """Test give_raise() method with custom raise amount."""
    emp = Employee("Jane", "Smith", 60000)
    emp.give_raise(10000)
    assert emp.annual_salary == 70000


def new_employee():
    """Create a new employee instance."""
    return Employee("Alice", "Johnson", 70000)

def test_give_default_raise_with_fixture(new_employee):
    """Test give_raise() method with default raise amount using a fixture."""
    new_employee.give_raise()
    assert new_employee.annual_salary == 75000

def test_give_custom_raise_with_fixture(new_employee):
    """Test give_raise() method with custom raise amount using a fixture."""
    new_employee.give_raise(15000)
    assert new_employee.annual_salary == 85000
