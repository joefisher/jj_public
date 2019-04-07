class Employee:
    def __init__(self,fname,lname,pay):
    self.fname = fname
    self.lname = lname
    self.pay = pay
    self.email = fname + '.' + lname + '@company.com'

def fullname(self):
    return'{} {}'.format(self.fname, self.lname)

emp_1.Employee('Juliette', 'Emge', 100000)
emp_2.Employee('Joe', 'Fisher', 200000)
emp_3.Employee('Jade', 'Fisher', 202000)

emp_1.fullname()
print(Employee.fullname(emp_1))