#!/usr/bin/python3
import paytest
import disgruntled


salary_employee = paytest.SalaryEmployee(1, "Micheline Larbinos", 1650)
hourly_employee = paytest.HourlyEmployee(2, "Jane Labidouille", 140, 15)
commission_employee = paytest.CommissionEmployee(3, "Jean-Michmuch Véherpé", 1200, 1250)
disgruntled_employee = disgruntled.DisgruntledEmployee(20000, "Roland Culé")

payroll_system = paytest.PayrollSystem()
payroll_system.calculate_payroll(
    [
        salary_employee,
        hourly_employee,
        commission_employee,
        disgruntled_employee,
        ]
)