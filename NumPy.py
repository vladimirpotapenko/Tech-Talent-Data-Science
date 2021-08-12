# Q1

import numpy as np

def arrays(arr):
    '''This function takes in a list from the input function and converts the
    provided space separated integers as a reversed numpy ndarray object
    with float type elements'''
    
    arr = np.array(arr,dtype=float)
    print(arr[::-1])
    print(type(arr[0]))

arr = input("Please enter a series of spaced separated integers: ").strip().split(' ')

arrays(arr)


# Q2

import numpy as np


def poly_loc_val():
    '''This function takes in the coefficients of a polynomial as well as a
    location argument and returns the value of the polynomial evaluated at the
    location'''
    
    coeff = input("Please input the (space-separated) coefficients of your polynomial: ").strip().split(' ')
    coeff = np.array([float(x) for x in coeff])
    point = int(input("Please enter the point where you want to evaluate: "))
    value = np.polyval(coeff,point)
    print(value)

poly_loc_val()