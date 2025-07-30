from salary import Salary

class Employee:
    def __init__(self, name, salary_amount):
        self.name = name
        self.salary = Salary(salary_amount)

    def get_employee_details(self):
        return f"Name: {self.name}, Salary: {self.salary.amount}"
