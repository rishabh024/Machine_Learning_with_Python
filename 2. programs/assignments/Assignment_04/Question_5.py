# Developed By : Rishabh Gupta

# Question is-  Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

def factorial_no (a):
    f = 1
    while(a>0):
        f = f * a
        a -= 1
    return f

if __name__ == "__main__":
    a = eval(input("enter any no--"))
    print("factorial_no is-", factorial_no(a))
