# find roots of quadratic eq. by using dharacharya formula
# convert math formula to python expression

# get a,b,c from user
a = eval(input("enter a-"))
b = eval(input("enter b-"))
c = eval(input("enter c-"))

numerator = (-b + (((b ** 2) - 4 * a * c) ** 0.5))

if (type(numerator) is not complex):
    print(numerator // (2 * a))
else:
    print(numerator, '/', 2 * a)  # complex value is printed in parenthesis
