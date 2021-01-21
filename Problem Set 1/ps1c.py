""" 
MIT 6.0001 Introduction to Computer Science and Programming in Python

Problem Set 1 -- Part C

Assuming user input is correct.

"""


# user input
annual_salary = int(input("Enter your annual salary: "))

annual_salary_orig = annual_salary

# initializing values
total_cost = 1000000
semi_annual_raise = 0.07
r = 0.04
steps = 0
low = 0.0 
high = 1.0
guess = (high + low)/2.0
three_years = 36
number_of_months = 0

# intermediate calculations
current_savings = 0
number_of_months = 0
annual_salary = annual_salary_orig
monthly_salary = annual_salary/12
investment_amount = monthly_salary * guess
portion_down_payment = total_cost * 0.25
old_guess = 0.0

epsilon = 0.01

while abs(guess - 1.0) >= epsilon:

    while number_of_months < three_years:
        current_savings = current_savings + (current_savings*0.04)/12 + investment_amount
        number_of_months = number_of_months + 1

        if number_of_months % 6 == 1:
            if number_of_months != 1:
                annual_salary = annual_salary + (annual_salary*semi_annual_raise)
                monthly_salary = annual_salary/12
                investment_amount = monthly_salary * guess


    if current_savings < portion_down_payment:
        low = guess
    else:
        high = guess

    print('High:', high)
    print('Low:', low)





    guess = (high + low)/2.0 
    steps = steps + 1
    number_of_months = 0
    current_savings = 0
    annual_salary = annual_salary_orig    
    monthly_salary = annual_salary/12
    investment_amount = 0    
    
    
        
print("Best savings rate: ", guess)
print("Steps in bisection search", steps)

