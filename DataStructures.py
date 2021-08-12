#Q1

import math

def solve_quadratic(a,b,c):
    '''Function that takes in three numbers and returns quadratic roots'''
    
    sqrtval = (b**2) - (4*a*c)
    if sqrtval < 0:
        print(f"The values of {a}, {b}, {c} do not compute in this formula")
    else:
        pos_val = (-b + math.sqrt(sqrtval))/(2*a)
        neg_val = (-b - math.sqrt(sqrtval))/(2*a)
        return (neg_val, pos_val)
    
    
#Q2

UserTupleInput = input("Please provide integers separated by a space: ")
InputSplit = UserTupleInput.split()
IntSplit = []
for item in InputSplit:
    i = int(item)
    IntSplit.append(i)
Tup = tuple(IntSplit)
HashTup = hash(Tup)
print(HashTup)

#Q3

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28] 
listThree = listOne[1:len(listOne):2] + listTwo[2:len(listTwo):2]
print(listThree)

#Q4

sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
width = len(sampleList)
x,y,z = sampleList[0:width:3], sampleList[1:width:3], sampleList[2:width:3]
print(x)
print(y)
print(z)

#Q5

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
rollcopy = sorted(rollNumber)
sampleDict = {'Zach':47, 'Emma':69, 'Kelly':76, 'Jason':97}
for number in rollcopy:
    if number not in sampleDict.values():
        rollNumber.remove(number)
print(rollNumber)

#Bonus1

z = ([2,3],4)
zz = ([4,44,4444],[5,6])
zzz = ("hello dolly","kitty","franchise")


def tup_func(tup):
    '''This function does the appending to a list to be able
    to get to the necessary values in future programs'''
    
    if type(tup) != tuple:
        raise TypeError("Only tuples will be accepted")
    
    lst = []
    for element in tup:
        if len(str(element)) > 1:
            lst.extend([str(part) for part in element])
        else:
            lst.append(str(element))
    return lst


def tuple_to_string(tup):
    '''This function converts a tuple to a string
    by way of creating a list, using append, and then
    using the join method for strings'''
    
    tup_list = []
    for element in tup:
        element_conv = str(element)
        tup_list.append(element_conv)
    return "".join(tup_list)


def tup2(tup):
    '''This function converts a tuple to a string through
    the use of an generator expression that creates an iterator'''
    
    z = (str(element) for element in tup)
    return "".join(z)

def tup3(tup):
    '''Function takes in tuple and returns string, but focuses
    more on tuples with lists as elements'''
    
    lst = []
    for element in tup:
        if len(str(element)) > 1:
            for part in element:
                lst.append(str(part))
        else:
            lst.append(str(element))
    
    return "".join(lst)
        
###This is the best one I have for this, others were building up

def tup4(tup):
    '''Function takes in tuple and returns string, but focuses
    more on tuples with lists as elements and list comprehension'''
    
    lst = tup_func(tup)
    
    return "".join(lst)     

#Bonus2

def check_tuple(looking_for, looking_in):
    '''Function checks to see if what we are (looking_for) is in a tuple 
    known as the object we are (looking_in)'''
    
    if type(looking_in) != tuple:
        raise TypeError("Only tuples will be accepted")
    
    default = "off"
    for item in looking_in:
        if len(str(item)) > 1:
            if looking_for in item:
                print("Yes, it's there")
                default = "on"
                break
            elif looking_for == item:
                print("Yep, it's there")
                default = "on"
                break
        elif looking_for == item:
                print("Sure, it's there")
                default = "on"
                break
    
    if default == "off":
        print("No, it's not there")
        
#Bonus3

def tup_format(tup):
    '''This function takes a tuples and creates a string
    through string formatting. Strings will be broken down into
    individual characters'''
    
    format_items = tup_func(tup)
    string_to_format = f"The elements are {format_items}"
    return string_to_format

