# Q1

import math

class Complex(object):
    '''This class is for complex numbers and provides a number of arithmetic
    operations'''
    
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        self.complx = complex(self.real, self.imaginary)
        
    def __add__(self, no):
        real_part = self.real + no.real
        imaginary_part = self.imaginary + no.imaginary
        #complex_add = complex(real_part, imaginary_part)
        return f"\n{real_part:-.2f}{imaginary_part:+.2f}i"
        
    def __sub__(self, no):
        real_part = self.real - no.real
        imaginary_part = self.imaginary - no.imaginary
        #complex_sub = complex(real_part, imaginary_part)
        return f"{real_part:-.2f}{imaginary_part:+.2f}i"
        
        
    def __mul__(self, no):
        real_part = ((self.real*no.real) - (self.imaginary*no.imaginary))
        imaginary_part = ((self.real*no.imaginary) - (no.real*self.imaginary))
        #complex_mul = complex(real_part, imaginary_part)
        return f"{real_part:-.2f}{imaginary_part:+.2f}i"
    
    def __truediv__(self, no):
        numerator = self.complx
        denominator = no.complx
        complx_cnj = denominator.conjugate()
        numerator *= complx_cnj
        denominator *= complx_cnj
        complex_div = numerator/denominator
        return f"{complex_div.real:-.2f}{complex_div.imag:+.2f}i"
        
    def mod(self):
        modulo = math.sqrt(((self.real**2)+(self.imaginary**2)))
        return f"{modulo:.2f}+0.00i"
        
    def __str__(self):
        return "This is how the Complex class operates!"

        
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
    
    