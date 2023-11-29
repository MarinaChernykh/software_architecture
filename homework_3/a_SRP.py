# Переписать код в соответствии с Single Responsibility Principle:
# ​Подсказка: вынесите метод calculateNetSalary() в отдельный класс


class Employee:
    def __init__(self, name, dob, base_salary):
        self.name = name
        self.dob = dob
        self.base_salary = base_salary

    def get_emp_info(self):
        return f"name - {self.name} , dob - {self.dob}"


class Salary:
    def __init__(self, employee):
        self.employee = employee

    def calculate_net_salary(self):
        tax = int(self.employee.base_salary * 0.25)
        return self.employee.base_salary - tax


# НИЖЕ - ПЕРВОНАЧАЛЬНЫЙ КОД
# class Employee:
#     def __init__(self, name, dob, base_salary):
#         self.name = name
#         self.dob = dob
#         self.base_salary = base_salary

#     def get_emp_info(self):
#         return f"name - {self.name} , dob - {self.dob}"

#     def calculate_net_salary(self):
#         tax = int(self.base_salary * 0.25)  # рассчитать налог другим способом
#         return self.base_salary - tax
