# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sofia Rodriguez
# Section:      536
# Assignment:   Lab 6.17
# Date:         09 27 2024

#get integers from user
a = input('Enter an integer: ')
b = input('Enter another integer: ')

#add up sums
num = int(a)
sum = 0
while num <= int(b):
    sum += int(num)
    num += 1

print('The sum of all integers from', a, 'to', b,'is', sum)
