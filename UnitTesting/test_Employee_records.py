import unittest
from Employee_records import Employee

class Test_Employee_Records(unittest.TestCase):
    def test_employee_email(self):
        employee_1 = Employee("Harry", "Doug", 50000)
        employee_2 = Employee("Mary", "Albert", 65000)
        self.assertEqual(employee_1.employee_email, "harrydoug@gmail.com")
        self.assertEqual(employee_2.employee_email, "maryalbert@gmail.com")

        employee_1.fname = "Marcel"
        employee_2.lname = "Damarol"
        self.assertEqual(employee_1.employee_email, "marceldoug@gmail.com")
        self.assertEqual(employee_2.employee_email, "marydamarol@gmail.com")

    def test_employee_fullname(self):
       employee_1 = Employee("Harry", "Doug", 50000)
       employee_2 = Employee("Mary", "Albert", 65000)
       self.assertEqual(employee_1.employee_fullname, "Harry Doug")
       self.assertEqual(employee_2.employee_fullname, "Mary Albert")

       employee_1.fname = "Marcel"
       employee_2.lname = "Damarol"
       self.assertEqual(employee_1.employee_fullname, "Marcel Doug")
       self.assertEqual(employee_2.employee_fullname, "Mary Damarol")

    def test_employee_raised_pay(self):
        employee_1 = Employee("Harry", "Doug", 50000)
        employee_2 = Employee("Mary", "Albert", 65000)
        self.assertEqual(employee_1.employee_raised_pay, 52500)
        self.assertEqual(employee_2.employee_raised_pay, 68250)

if __name__ == '__main__':
    unittest.main()
