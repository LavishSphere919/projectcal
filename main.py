import math
from fractions import Fraction as frac

print('Welcome to the Calculator!')
while True:
    print(
        '1 - addition, 2 - division, 3 - multiplication, 4 - subtraction, 5 - square root, 6 - exponentiation, 7 - percent-number, 8 - fraction, 9 - cube root, 0 - nth root, 10 - number-percent, 00 - sin, 01 - cos, 02 - tan, i - info'
    )
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
            "Created by: Ashsmith Khayrul Version: 1.0.0.0.1 Last updated: Saturday, October 30th, 2021 at 3:47 PM PDT Python 3.8.2 Feb 26, 2020 02:56:10"
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
    else:
        print('Value not found.')
