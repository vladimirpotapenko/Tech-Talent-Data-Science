#Q1

import random

def RandGuessFunc():
    '''This function takes in a user defined integer and then guesses that
    value'''
    
    UserInput = input("Please pick an integer between 1 and 10 (INCLUSIVE) ")
    guess = random.randint(1,10)
    if guess is int(UserInput):
        print(f"Our guess is {guess}. Lucky for us, it's right!")
    else:
        print(f"Our guess is {guess}, but that seems to be wrong")
    
    
RandGuessFunc()
    
#Q2

import re

flag = 0

UserPassword = input('''Please provide a valid password
                     
Passwords are:
    
    At least 1 letter between [a-z] 
    and 1 letter between[A-Z]
    At least 1 number between [0-9]
    At least 1 character from [$#@]
    Minimum length 6 characters
    Maximum length 16 characters
    
Your Password: ''')
    
if not re.search(r"[a-z]", UserPassword):
    flag = 1

if not re.search(r"[A-Z]", UserPassword):
    flag = 1
    
if not re.search(r"[0-9]", UserPassword):
    flag = 1

if not re.search(r"[$#@]", UserPassword):
    flag = 1

if not len(UserPassword) >= 6:
    flag = 1

if not len(UserPassword) <= 16:
    flag = 1
    
if flag == 0:
    print("Your password is valid")
else:
    print("Your password is invalid")

#Q3

UserInputFriends = input("Hey, can you name three of your friends? Please input with a space between values ")
UserInputFrAges = input("How old are they? Please input with a space between values ")
Friends = UserInputFriends.split()
Ages = UserInputFrAges.split()
AgesLst = [int(x) for x in Ages]
OldestAge, YoungestAge = max(AgesLst), min(AgesLst)
OldestFriend, YoungestFriend = (Friends[AgesLst.index(OldestAge)], 
                                Friends[AgesLst.index(YoungestAge)])
print(f"I dont know if you know this, but your oldest friend is {OldestFriend}",
f"who happens to be {OldestAge}, while your youngest friend is",
f"{YoungestFriend} who is {YoungestAge}")

#Q4

NumClasses = input("Enter the number of classes held: ")
AttClasses = input("Enter the number of classes attended: ")
ClassPerc = int(AttClasses)/int(NumClasses)
if ClassPerc < .75:
    print(f"The student attended only {ClassPerc*100}% of their classes.",
          f"They WILL NOT be allowed to sit for the exam.")
else:
    print(f"The student attended {ClassPerc*100}% of their classes.",
          f"They WILL be allowed to sit for the exam.")

#Q5

N = int(input("Please provide any integer: "))
if N % 2 == 1:
    print("weird")
elif N % 2 == 0 and N in range(2,6):
    print("Not Weird")
elif N % 2 == 0 and N in range(6,21):
    print("Weird")
elif N % 2 == 0 and N > 20:
    print("Not Weird")
else:
    pass

#Bonus1

def string_reverse(string):
    '''This function reverses a string'''
    
    if type(string) != str:
        raise TypeError("Only strings will be accepted")
    
    reverse = string[::-1]
    
    return reverse


print(string_reverse("12345abcde"))

#Bonus2

import math as m

def tup_func(lst):
    '''This function does the appending to a list to be able
    to get to the necessary values in future programs'''
    
    if type(lst) != list:
        raise TypeError("Only lists will be accepted")
    
    lst_new = []
    for element in lst:
        if len(str(element)) > 1:
            lst_new.extend([part for part in element])
        else:
            lst_new.append(element)
    return lst_new

def mult_list(lst):
    '''This function multiplies all the elements of a list together
    and returns the product. Assuming we will not accept strings
    in our list'''
    
    lst_new = tup_func(lst)
    
    if any([type(item) == str for item in lst_new]):
        raise TypeError("Strings will not be accepted")
    else:
        product = m.prod(lst_new)
    
    return product

#Bonus3

import re


def case_count(string):
    '''This function takes in a string and returns the count of upper
    and lower case letters'''
    
    if type(string) != str:
        raise TypeError("Only strings will be accepted")
    
    uppercase = re.compile(r'[A-Z]')
    lowercase = re.compile(r'[a-z]')
    
    upper = re.findall(uppercase, string)
    lower = re.findall(lowercase, string)
    
    return  f'''
            The number of uppercase letters is: {len(upper)}
            The number of lowercase letters is: {len(lower)}'''

        
    

        