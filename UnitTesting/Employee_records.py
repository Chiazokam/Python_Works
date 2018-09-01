class Employee:
    raise_amt = 1.05
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay
    @property
    def employee_email(self):
        return '{}{}@gmail.com'.format(self.fname.lower(), self.lname.lower())
    @property
    def employee_fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    @property
    def employee_raised_pay(self):
        return int(self.pay * self.raise_amt)
