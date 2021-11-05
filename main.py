# Advanced Calculator created by Ash - V1 [Alpha]
# Most recent replit Python version used as of November, 2021
# Uses import function and other functions not found in Python 2
# Requires at least Python 3 or higher
# Great for Integrated II+ math requiring scientific calculator
import math
from fractions import Fraction as frac

print('Welcome to the Calculator!')
while True:
    print('1 - addition')
    print('2 - division')
    print('3 - multiplication')
    print('4 - subtraction')
    print('5 - square root')
    print('6 - exponentiation')
    print('7 - percent-number')
    print('8 - fraction')
    print('9 - cube root')
    print('0 - nth root')
    print('10 - number-percent')
    print('00 - sin')
    print('01 - cos')
    print('02 - tan')
    print('03 - tan^-1')
    print('04 - cos^-1')
    print('05 - sin^-1')
    print('i - info')
    operation = input('Value: ')
    if operation == '1':
        addendA = float(input('Please enter the first addend: '))
        addendB = float(input('Please enter the second addend: '))
        sum = addendA + addendB
        print('The sum for this problem is:', sum, '.')
    elif operation == '2':
        divisor = float(input('Please enter the divisor: '))
        dividend = float(input('Please enter the dividend: '))
        quotient = divisor / dividend
        print('The quotient for this problem is:', quotient, '.')
    elif operation == '3':
        multiplier = float(input('Please enter the multipler: '))
        multiplicand = float(input('Please enter the multiplicand: '))
        product = multiplier * multiplicand
        print('The product for this problem is', product, '.')
    elif operation == "4":
        minuend = float(input('Please enter the minuend: '))
        subtrahend = float(input('Please enter the subtrahend: '))
        difference = minuend - subtrahend
        print('The difference for this problem is', difference, '.')
    elif operation == "5":
        num1 = float(input('Please enter a number to find the square root: '))
        root = math.sqrt(num1)
        print('The square root for this value is: ', root, '.')
    elif operation == "6":
        base = float(input('Please enter the base: '))
        exponent = float(input('Plese enter the exponent: '))
        answer = base**exponent
        print('The answer for this problem is:', answer, '.')
    elif operation == "7":
        percentage = float(input('Please enter the percentage: '))
        numb = percentage / 100
        print('The number form for this problem is', numb, '.')
    elif operation == "8":
        numbe = input('Please enter the value: ')
        print(frac(numbe))
    elif operation == "i":
        print(
            "Created by: Ash Version: 1.0.0.0.2 Last updated: Thursday, November 4th, 2021 at 3:20 PM PDT Python 3.8.2 Feb 26, 2020 02:56:10"
        )
    elif operation == "9":
        num = float(input('Please enter a number to find the cube root: '))
        root2 = num**(1 / 3)
        print('The cube root for this value is:', root2, '.')
    elif operation == "0":
        num2 = float(input('Please enter a number to find the nth root: '))
        nth = float(input('Please enter the nth root: '))
        root3 = num2**(1 / nth)
        print('The solution is:', root3, '.')
    elif operation == "10":
        num0 = float(input('Please enter the number: '))
        percent = num0 * 100
        print('The percent form for this problem is', percent, '%.')
    elif operation == "00":
        sin = float(input('Plese enter the degree(s): '))
        degrees = math.sin(math.radians(sin))
        print('The sin for this number of degrees is', degrees, '.')
    elif operation == "01":
        cos = float(input('Please enter the degree(s): '))
        deg = math.cos(math.radians(cos))
        print('The cos for this number of degrees is', deg, '.')
    elif operation == "02":
        tan = float(input('Please enter the degree(s): '))
        degr = math.tan(math.radians(tan))
        print('The tan for this number of degrees is', degr, '.')
    elif operation == "03":
        atan = float(input('Please enter the degree(s): '))
        degree = math.atan(atan) * 57.2957795
        print('The tan^-1 for this number of degrees is', degree, '.')
    elif operation == "04":
        acos = float(input('Please enter the degree(s): '))
        if -1 <= acos <= 1:
            d = math.acos(acos) * 57.2957795
            print('The cos^-1 for this number of degrees is', d, '.')
        else:
            print('Degree(s) must be within range -1 to 1.')
    elif operation == "05":
        asin = float(input('Please enter the degree(s): '))
        if -1 <= asin <= 1:
            de = math.asin(asin) * 57.2957795
            print('The sin^-1 for this number of degrees is', de, '.')
        else:
            print('Degree(s) must be within range -1 to 1.')
    else:
        print('Value not found.')