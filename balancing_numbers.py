# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sofia Rodriguez
# Section:      536
# Assignment:   Lab 6.21
# Date:         09 27 2024

import math 

input = int(input('Enter a value for n: '))

#find if input is a balancing number
a = (8 * (input**2)) + 1
b = math.sqrt(a)
if b == int(b):
    r = (((-2*input) - 1) + b) / 2
    print(f'{input} is a balancing number with r={r:.0f}')
else:
    print(input, 'is not a balancing number')

#sum of all numbers before input
n = 1
sum = 0
while n < input:
    sum += n
    n += 1