def is_leap(year):
    leap = False
    
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return leap



n = int(input())

for numero in range(n):
    numero2 = numero * numero 
    print (numero2)

a = int(input())
b = int(input())

div = a // b
res = a / b

print (div)
print (res)


a = int(input())
b = int(input())

soma = a + b
diferenca = a - b
produto = a * b 

print (soma)
print (diferenca)
print (produto)
 

 import math
import os
import random
import re
import sys


n = int(input().strip())

if (n % 2 != 0):
    print('Weird')
    
elif n >= 6 and n <= 20:
    print('Weird') 
    
elif n >= 2 and n <= 5:
    print('Not Weird')     
    
else:
    print ('Not Weird')          
    
    