# Developed By : Rishabh Gupta

# Question is-  Write a Python function that that prints out the first n rows of Pascal's triangle


def factorial(a):
    f = 1
    while(a > 0):
        f = f * a
        a -= 1
    return f


def pascal_triangle(n):
    for i in range(0, n):
        for j in range(0, (n - i - 2)+1):
            print(".", end="")

        for j in range(0, (i)+1):
            no = factorial(i) / (factorial(j) * factorial(i-j))
            print(int(no), end="")

        print()


if __name__ == '__main__':
    a = eval(input("enter no of rows, you want in Pascal's triangle - "))
    pascal_triangle(a)
