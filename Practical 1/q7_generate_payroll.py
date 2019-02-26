
import math


def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier


# Empty dictionary
payroll = {'Name': '',
           'Weekly hours worked': '',
           'Hourly pay': '',
           'Gross pay': '',
           'CPF contribution': '',
           'Net pay': '',
           }

# Input name
name = input('Enter name here ')
payroll['Name'] = name

# Input hours worked
hrs_worked = float(input('Enter hours worked here '))
payroll['Weekly hours worked'] = hrs_worked

# Calculate pay per hour
hrs_pay_input = float(input('Enter hourly pay here '))
hrs_pay_input = round_up(hrs_pay_input, 2)
payroll['Hourly pay'] = hrs_pay_input

# Calculate gross pay
total_pay = float(hrs_pay_input * hrs_worked)
total_pay = round_up(total_pay, 2)
payroll['Gross pay'] = total_pay

# Input CPF contribution
CPF = float(input('Enter CPF contribution rate(%) here '))
CPF_float_percentage = CPF/100

# CPF contribution calculation
CPF_contribution = total_pay * CPF_float_percentage
CPF_contribution = round_up(CPF_contribution, 2)
payroll['CPF contribution'] = CPF_contribution

# Net pay calculation
net_pay = total_pay - CPF_contribution
payroll['Net pay'] = net_pay

# Print answer
print('Payroll statement for ', payroll['Name'])
for key,value in payroll.items():
print(payroll)
