#composition (composed at class level)
class Salary:
    def __init__(self,pay):
        self.pay=pay

    def get_total(self):
       return (self.pay*12)

class Employee:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus
        self.obj_salary=Salary(self.pay)

    def annual_salary(self):
        return "Total: "  +  str(self.obj_salary.get_total()+self.bonus)


obj_emp=Employee(100,10)
print (obj_emp.annual_salary())  #1210

#aggregation (at object level)
class Salary:
    def __init__(self,pay):
        self.pay=pay

    def get_total(self):
       return (self.pay*12)

class Employee:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return "Total: "  +  str(self.pay.get_total()+self.bonus)


obj_sal=Salary(100)
obj_emp=Employee(obj_sal,10)
print (obj_emp.annual_salary()) #1210
