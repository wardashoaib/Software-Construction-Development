def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_rate):
    return gross_salary * tax_rate / 100


def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax


name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
tax_rate = float(input("Enter tax rate: "))

gross = calculate_gross_salary(basic, allowance)
tax = calculate_tax(gross, tax_rate)
net = calculate_net_salary(gross, tax)

print("Employee Name:", name)
print("Gross Salary:", gross)
print("Tax:", tax)
print("Net Salary:", net)