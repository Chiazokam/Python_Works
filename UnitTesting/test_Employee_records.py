import unittest
from Employee_records import Employee

class Test_Employee_Records(unittest.TestCase):
    #The code within the setUp runs before any single test
    def setUp():
        #So we can define our object here and avoid definition in every test
        #These create two objects of the Employee class, then we test them out
        #Use the self. to set as instancce attributes
        self.self.employee_1 = Employee("Harry", "Doug", 50000)
        self.self.employee_2 = Employee("Mary", "Albert", 65000)

    #The code within this function runs after every soingle test
    def tearDown():
        pass
    def test_employee_email(self):
        #self.assertEqual(self.employee_1.employee_email, "harrydoug@gmail.com")
        #self.assertEqual(self.employee_2.employee_email, "maryalbert@gmail.com")
        self.employee_1.fname = "Marcel"
        self.employee_2.lname = "Damarol"
        self.assertEqual(self.employee_1.employee_email, "marceldoug@gmail.com")
        self.assertEqual(self.employee_2.employee_email, "marydamarol@gmail.com")

    def test_employee_fullname(self):
       #self.employee_1 = Employee("Harry", "Doug", 50000)
       #self.employee_2 = Employee("Mary", "Albert", 65000)
       self.assertEqual(self.employee_1.employee_fullname, "Harry Doug")
       self.assertEqual(self.employee_2.employee_fullname, "Mary Albert")

       self.employee_1.fname = "Marcel"
       self.employee_2.lname = "Damarol"
       self.assertEqual(self.employee_1.employee_fullname, "Marcel Doug")
       self.assertEqual(self.employee_2.employee_fullname, "Mary Damarol")

    def test_employee_raised_pay(self):
        #self.employee_1 = Employee("Harry", "Doug", 50000)
        #self.employee_2 = Employee("Mary", "Albert", 65000)
        self.assertEqual(self.employee_1.employee_raised_pay, 52500)
        self.assertEqual(self.employee_2.employee_raised_pay, 68250)

if __name__ == '__main__':
    unittest.main()
