# Q1

def leap_year_check():
    '''This function takes in a year as input from the user and checks if it
    is a leap year'''
    
    try:
        year = int(input("Please provide a year for us to check: "))
        not_leap = f"{year} is not a leap year"
        leap = f"{year} is a leap year"
    except ValueError as v:
        print("Please make sure to be entering integers:", v)
    else:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f'{leap}')
                else:
                    print(f'{not_leap}')
            else:
                print(f'{leap}')
        else:
            print(f'{not_leap}')
                    
#leap_year_check()

# Q2

def div_check(a,b):
    '''This function computes integer division between two values, with an
    error being raised for improper values'''
    
    try:
         div_val = int(a)/int(b)
    except ZeroDivisionError as z:
        print("ZeroDivionError:", z)
    except ValueError as v:
        print("ValueError:", v)
    else:
        print(div_val)

#Another way to do this; not a function

val1 = input("Please enter a value: ")
val2 = input("Please enter another value to divide the first by: ")

try:
    div_val = int(val1)/int(val2)
except ZeroDivisionError as z:
    print("ZeroDivionError:", z)
except ValueError as v:
    print("ValueError:", v)
else:
    print(div_val)


#Bonus1

prompt_string = '''
Please provide any number of values, with each separated by a comma:\n 
'''

user_list = input(prompt_string).split(',')
try:
    new_list = [int(x) for x in user_list if x != ',']
except ValueError as v:
    print("ValueError, please enter proper input:", v)
else:
    order = 0
    for num in new_list:
        if order != (len(new_list) - 1):
            print(num)
            new_list[order] = 0
            order += 1
        else:
            print(num)


#Bonus2

lst1 = list(input('''
Please provide any number of values separated by a comma: '''))

try:
    out_of_bounds_val = lst1[len(lst1)]
except IndexError as ie:
    print("IndexError:", ie)
    
#Bonus3

import re

pattern = re.compile(r'[0-9]+\.?[0-9]*')

user_input = input('''
Please provide a list of integers separated by a comma: ''')

new_list = re.findall(pattern, user_input)
float_list = [float(num) for num in new_list if '.' in num]
int_list = [int(num) for num in new_list if '.' not in num]
final_list = sorted(int_list + float_list)
for val in final_list:
    if val > 150:
        break
    elif val % 5 == 0:
        print(val, end=' ')
    else:
        continue







