'''The Python math module offers you the ability to perform common and useful mathematical calculations within your
application like-

Calculating combinations and permutations using factorials
Calculating the height of a pole using trigonometric functions
Calculating radioactive decay using the exponential function
Calculating the curve of a suspension bridge using hyperbolic functions
Solving quadratic equations
Simulating periodic functions, such as sound and light waves, using trigonometric functions

Since the math module comes packaged with the Python release, you don’t have to install it separately.
Just import math module:-   '''

import math


''' Various predefined constants of the math Module are:-

1) Pi (π) -
Pi (π) is the ratio of a circle’s circumference (c) to its diameter (d):- (π = c/d)
This ratio is always the same for any circle. It is an irrational number.
Therefore, pi has an infinite number of decimal places, but it can be approximated as 22/7, or 3.141.
It has its own celebration date, called Pi Day, which falls on March 14th (3/4 feature selction).'''


r = int(input("enter radius of circle:-"))
circumferenceOfCircle = 2 * math.pi * r
print("circumference of circle is:- ", format(circumferenceOfCircle, "6.4f"))


'''
2) Tau (τ)-
Tau (τ) is the ratio of a circle’s circumference to its radius. Tau = 2pi or roughly 6.28.
Tau is also an irrational number because it’s just pi times two. '''

circumferenceOfCircle = math.tau * r
print("circumference of circle is:- ", circumferenceOfCircle)


'''
3) e -
Euler’s number (e) is a constant that is the base of the natural logarithm.
Euler’s number is an important constant because it has many practical uses, such as calculating population growth
over time or determining rates of radioactive decay. It is also an irrational number.
The value of e is often approximated as 2.718.
'''

print("Euler's number is- ", math.e)

'''
Note - The value of math.e, math.pi and math.tau is given to fifteen decimal places and is returned as
a float value.'''

'''
4) ∞ -
Infinity can’t be defined by a number. Rather, it’s a mathematical concept representing something that is
never-ending or boundless or which is not in our capacity. Infinity can go in either direction, positive or negative.
We can use infinity in algorithms when we want to compare a given value to an absolute maximum or minimum value. '''

print("pos. inf is:", math.inf)
print("neg inf is:", -math.inf)

'''
Note - No number can be greater than infinity or smaller than negative infinity. That’s why mathematical operations
with math.inf don’t change the value of infinity
'''
print(math.inf + 1e308)
print("inf remains same after operation")


'''
5) NaN -
Not a number, or NaN, isn’t really a mathematical concept. It originated in the computer science field as a
reference to those values that are not numeric. NaN is occurred when-
a) non-numeric input is given
b) mathematical operations produce undefined result-
   i)   0÷0
   ii)  0*∞
   iii) ∞÷∞
'''
print("NaN value is-", math.nan)


'''Arithmetic Functions are:- '''

'''
1) factorial(x) -
It takes only positive integer x. It never takes negative or decimal numbers, then you will
get a ValueError: factorial() not defined for negative values.
'''
n = int(input("enter no. "))
print("factorial of ", n, " is: ", math.factorial(n))


'''
2) ceil(x) -
It will return the smallest next integer value that is greater than or equal to the given number x.
When you give integer value as input to ceil(), it will return the same number.
when string is given, then we get- TypeError: must be real number, not str
'''

print(math.ceil(5.43))
print(math.ceil(-12.43))
print(math.ceil(9))


'''
3) floor(x) -
It will return the greatest integer number that is less than or equal to the given number.
'''

print(math.floor(5.43))
print(math.floor(-5.43))
print(math.floor(9))


'''
4) trunc() -
If want to keep only the integer part and eliminate the decimal part from a real no. then use this method.
'''

print(math.trunc(12.32))
print(math.trunc(-43.24))

'''
Note-
1) Dropping the decimal value is a type of rounding. With trunc(), negative numbers are
always rounded upward toward zero and positive numbers are always rounded downward toward zero.
2) trunc() behaves the same as floor() for positive numbers.
3) trunc() behaves the same as ceil() for negative numbers.
'''


'''
5) isclose() -
It lets you to set your own tolerance, for closeness of 2 numbers.
It returns True if two numbers are within your established tolerance for closeness and otherwise returns False.

-> isclose() will return True when the following condition is satisfied:-
        ->  abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol).

There are 2 ways for defining closeness-
1) Relative tolerance, or rel_tol, is the maximum difference for being considered “close” relative of the magnitude
   of the input values. This is the percentage of tolerance. The default value is 1e-09 or 0.000000001
2) Absolute tolerance, or abs_tol, is the maximum difference for being considered “close” regardless of the
   magnitude of the input values. The default value is 0.0
Closeness is a relative concept only
'''

print(math.isclose(6, 7))   # False because the relative tolerance is set for nine decimal places by default
print(math.isclose(6.999999999, 7))     # True because the value 6.999999999 is within nine decimal places
print(math.isclose(6, 7, rel_tol=0.2))   # prints True


'''
6) pow(base value, power value) -
It raises x to some power y. You can give an integer or a decimal value as input and the function always returns
a float value.
'''
print(math.pow(1.0, 3))
print(math.pow(-4, 3))
print(math.pow(math.nan, 0.0))
print(math.pow(0.0, 2.3))

''' Note-
1) The (ValueError: math domain error) only occurs when the base is 0
2) Apart from math.pow(), there are two built-in ways of finding the power of a number in Python:
    a) x ** y  - When you use integers, you get an integer value. When you use decimal values, the return type
       changes to a decimal value.
    b) pow() - It is a versatile built-in function which gives int or decimal result based on input
       The built-in pow() method has three parameters:-
       1) The base number    -  mandatory arg
       2) The power number   -  mandatory arg
       3) The modulus number -  optional arg - It is often used in cryptography.
          It is equivalent to the equation (x ** y) % z.
          It is like this -> (32 ** 6) % 5 == pow(32, 6, 5)
    ->pow() raises the base (32) to the power (6), & then the result value is modulo divided by the modulus number (5)
3) The execution times for each method is different. math.pow() is faster & built-in pow() is the slowest.
4) The reason behind the efficiency of math.pow() is the way that it’s implemented. It relies on the underlying C language.
5) math.pow() can’t handle complex numbers, whereas pow() and ** can.
'''

print(pow(3, 2))
print(pow(2, 3.3))


'''
7) exp() -
Euler’s number is the base of the natural logarithm. When Euler’s number is incorporated into the exponential function,
it becomes the natural exponential function.

'''
print(math.exp(-1.2))

'''
Note-
1) The input number can be positive or negative, and the function always returns a float value.
If the number is not a numerical value, then the method will return a TypeError:must be real number, not str.
math.exp() is faster than the other methods and pow(e, x) is the slowest. This is the expected behavior because of
the underlying C implementation of the math module.
2) exp() is more accurate than the other two methods.
'''

print(math.e ** 4)
print(pow(math.e, 4))


'''
8) log(x) -
Logarithmic functions can be considered the inverse of exponential functions."logb x" (pronounced as "the logarithm of x to base b")
The natural logarithm of a number is its logarithm to the base of mathematical constant e(Euler’s number).It’s generally
depicted as f(x) = ln(x), where e is implicit.
log() has two arguments:- The first one is mandatory and the second one is optional.
Note-- We get (ValueError: math domain error) as log values are undefined for negative numbers and zero.
'''
# 1st ex - With one argument you can get the natural log (to the base e) of the input number
print(math.log(3.4))

# log(value, base):-
print(math.log(math.pi, 5))

# log2() is used to calculate the log value to the base 2
print(math.log2(math.pi))     # log2() is more accurate
print(math.log(math.pi, 2))

# log10() is used to calculate the log value to the base 10
print(math.log10(math.pi))      # log10() is more accurate
print(math.log(math.pi, 10))


'''
9) gcd()-
(GCD) of two positive numbers is the largest positive integer that divides both numbers.
We can give positive or negative numbers as input,& it returns the appropriate GCD value.But you can’t input a decimal number
'''
a = int(input("enter no"))
b = int(input("enter no"))
print("GCD is:-", math.gcd(a,b))

'''
10) fsum() -
If you ever want to find the sum of the values of an iterable without using a loop, then use this fnx.
You can use iterables such as arrays, tuples, or lists as input and the function returns the sum of the values.
Note - fsum() is more accurate than sum().
'''
b = [1, 2, 3, 4, 5]
print("sum of iterable is-", math.fsum(b))

'''
1 load data) sqrt() -
Give positive real number (integer or decimal). It always returns a float value.
The function will throw a ValueError if you try to enter a negative number.
'''

print("sqrt of no is-", math.sqrt(a))

'''
2 data visualization) degrees() -
Angles can be measured either by degrees or by radians. Sometimes you have to convert degrees to radians and vice versa.
'''
d = int(input("enter degree"))
print("your radian is:-", math.radians(d))  # It returns the radian value of the degree input.
r = int(input("enter radians"))
print("your degree is:-", math.degrees(r))  # It convert radians to degrees


'''
Trigonometric methods -
'''
# math.sin()
# math.cos()
# math.tan()
# # to calculate arc sin-
# math.asin()
# math.acos()
# math.atan()
# # to calculate the hypotenuse of a triangle -
# math.hypot()


'''
The functions of the Python math module aren’t equipped to handle complex numbers. However, Python provides a different module 
that can specifically deal with complex numbers, the cmath module. 
The Python math module is complemented by the cmath module, which implements many of the same functions but for complex numbers.
'''

# cmath - complex math
# complex() used to create complex numbers
# import cmath
# c = 2 + 3j
# d = complex(2, 3)
# cmath.sqrt(c)
# cmath.log(c)
# cmath.exp(c)

