#!/usr/bin/python3
from abc import ABC, abstractmethod

class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Claculating Payroll")
        print("===================")
        for employee in employees:
            print("Payroll for: {} - {}".format(employee.id, employee.name))
            print("- Check amount: {}". format(employee.calculate_payroll()))
            print("")

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass

class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def calculate_payroll(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, monthly_salary, commission):
        super().__init__(id, name, monthly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission
