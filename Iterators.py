# Q1
import itertools as its

def cart_prod_func(lst1, lst2):
    '''This function provides a sorted list of cartesian products when given
    two lists'''
    
    length_check = (len(lst1) or len(lst2))
    if length_check < 1 or length_check > 30:
        print("Please ensure both lists have at least one, but fewer than 30",
              "elements")
    else:
        lst1.sort(), lst2.sort()
        cart_prod = its.product(lst1,lst2)
    
        return cart_prod

print(*cart_prod_func([0,2,1],[6,7,1]))

# Q2

import re
import itertools as its

pattern = re.compile(r'([A-Z]|[0-9]+)')

string_input = input("Please enter a string: ").upper()

letters_list = sorted(list(re.findall(pattern, string_input)))
letters_perm = its.permutations(letters_list)
for perm in letters_perm:
    str_perm = str(perm)
    print("".join(perm), end='\n')

 
    
# Q3

import re
import itertools as its

pattern = re.compile(r'([A-Z]|[0-9]+)')

str_input = input("Please enter a string: ").upper()
size_comb = int(input("Please enter an integer dictating combination size: "))

letters_list = list(re.findall(pattern, str_input))
letters_comb = sorted(list(its.combinations_with_replacement(letters_list, 
                                                             size_comb)))
for comb in letters_comb:
    str_comb = str(comb)
    print("".join(comb), end='\n')


#Bonus1

numbers = [1,2,3,-5,3,-100,2000]
newlist = [int(num) for num in numbers if num > 0]
print(newlist)
