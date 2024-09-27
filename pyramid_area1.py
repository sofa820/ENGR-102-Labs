# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sofia Rodriguez
# Section:      536
# Assignment:   Lab 6.11
# Date:         09 26 2024

import math
side = float(input('Enter the side length in meters: '))
num_layers = int(input('Enter the number of layers: '))

blocks = 0
num = num_layers
while num > 0: 
    blocks += (num ** 2) #blocks in a layer
    num -= 1

s_area_2 = 0
num_2 = num_layers
while num_2 > 0:
    blocks_2 = (num_2 ** 2)
    s_area_2 += (side**2 * (math.sqrt(blocks_2))*4) + (blocks_2 * (side**2))
    num_2 -= 1

num_3 = 1
s_area_3 = s_area_2
while num_3 < num_layers:
    blocks_3 = (num_3 ** 2)
    s_area_3 -= blocks_3 * (side ** 2)
    num_3 += 1

print(f'You need {s_area_3:.2f} m^2 of gold foil to cover the pyramid')
