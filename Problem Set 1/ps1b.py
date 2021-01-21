""" 
MIT 6.0001 Introduction to Computer Science and Programming in Python

Problem Set 1 -- Part B

Assuming user input is correct.

"""

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

monthly_salary = annual_salary / 12.0
portion_down_payment = total_cost * 0.25
r = 0.04
current_savings = 0
number_of_months = 0
investment_amount = monthly_salary * portion_saved


while current_savings < portion_down_payment:
    current_savings = current_savings + (current_savings*0.04)/12 + investment_amount
    number_of_months = number_of_months + 1
    
    if number_of_months % 6 == 1:
        if number_of_months != 1:
            annual_salary = annual_salary + (annual_salary*semi_annual_raise)
            monthly_salary = annual_salary/12
            investment_amount = monthly_salary * portion_saved
    

print("Number of months:", number_of_months)