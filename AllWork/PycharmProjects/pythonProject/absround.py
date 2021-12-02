

# Examples:
# Code Example 1: Integer and Float number
# testing abs() for an integer and float
int_num = -25
float_num = -10.50
print("The absolute value of an integer number is:", abs(int_num))
print("The absolute value of a float number is:", abs(float_num))

# Example 2: Complex Number
# testing abs() for a complex number
complex_num = (3 + 10j)
print("The magnitude of the complex number is:", abs(complex_num))

#--------------------------------------------------------------------------------------
# Round():Round() is a built-in function available with python. It will return you a float number that will be rounded to the decimal places which are given as input.
# If the decimal places to be rounded are not specified, it is considered as 0, and it will round to the nearest integer.

# Example 1: rounding vs truncating
import random


def truncate(num):
    return int(num * 1000) / 1000


arr = [random.uniform(0.01, 0.05) for _ in range(1000000)]
sum_num = 0
sum_truncate = 0
for i in arr:
    sum_num = sum_num + i
    sum_truncate = truncate(sum_truncate + i)

print("Testing by using truncating upto 3 decimal places")
print("The original sum is = ", sum_num)
print("The total using truncate = ", sum_truncate)
print("The difference from original - truncate = ", sum_num - sum_truncate)

print("\n\n")
print("Testing by using round() upto 3 decimal places")
sum_num1 = 0
sum_truncate1 = 0
for i in arr:
    sum_num1 = sum_num1 + i
    sum_truncate1 = round(sum_truncate1 + i, 3)

print("The original sum is =", sum_num1)
print("The total using round = ", sum_truncate1)
print("The difference from original - round =", sum_num1 - sum_truncate1)

#-------------------------------------------------------------------------------------------
# Example: Rounding Float Numbers
# testing round()

float_num1 = 10.60  # here the value will be rounded to 11 as after the decimal point the number is 6 that is >5

float_num2 = 10.40  # here the value will be rounded to 10 as after the decimal point the number is 4 that is <=5

float_num3 = 10.3456  # here the value will be 10.35 as after the 2 decimal points the value >=5

float_num4 = 10.3445  # here the value will be 10.34 as after the 2 decimal points the value is <5

print("The rounded value without num_of_decimals is :", round(float_num1))
print("The rounded value without num_of_decimals is :", round(float_num2))
print("The rounded value with num_of_decimals as 2 is :", round(float_num3, 2))
print("The rounded value with num_of_decimals as 2 is :", round(float_num4, 2))

#------------------------------------------------------------------------------------------
# Example: Rounding Integer Values
# testing round() on a integer

num = 15

print("The output is", round(num))

#------------------------------------------------------
# Example: Rounding on Negative Numbers
# testing round()

num = -2.8
num1 = -1.5
print("The value after rounding is", round(num))
print("The value after rounding is", round(num1))

#----------------------------------------------------------
# Example: Round Numpy Arrays
# testing round()
import numpy as np

arr = [-0.341111, 1.455098989, 4.232323, -0.3432326, 7.626632, 5.122323]

arr1 = np.round(arr, 2)

print(arr1)

#---------------------------------------------------------
# Example: Decimal Module
import decimal

round_num = 15.456

final_val = round(round_num, 2)

# Using decimal module
final_val1 = decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_CEILING)
final_val2 = decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_DOWN)
final_val3 = decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_FLOOR)
final_val4 = decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_DOWN)
final_val5 = decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_EVEN)
final_val6 = decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_HALF_UP)
final_val7 = decimal.Decimal(round_num).quantize(decimal.Decimal('0.00'), rounding=decimal.ROUND_UP)

print("Using round()", final_val)
print("Using Decimal - ROUND_CEILING ", final_val1)
print("Using Decimal - ROUND_DOWN ", final_val2)
print("Using Decimal - ROUND_FLOOR ", final_val3)
print("Using Decimal - ROUND_HALF_DOWN ", final_val4)
print("Using Decimal - ROUND_HALF_EVEN ", final_val5)
print("Using Decimal - ROUND_HALF_UP ", final_val6)
print("Using Decimal - ROUND_UP ", final_val7)