# triangular no is the summation from 1 to the given no = total no of dots in nth triangle
# triangular no. sequence - 1,3,6,10,5 data separation(split),21,28...
# each term of this sequence represents the no of dots in each triangular pattern
# to get no of dots in a nth triangle,formula is -> n(n+1)/2 = (summation from 1 to nth no) = (linear summation formula)

# find the no of dots in a nth triangle, where value of n given by user

n = eval(input("enter n -"))
print("total no of dots/triangular number for", n, "th triangle is -", (n * (n + 1)) // 2)
