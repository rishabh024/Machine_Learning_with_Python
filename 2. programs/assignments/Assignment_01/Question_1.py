# Developed By : Rishabh Gupta

# Question is- Print Alphabet Pattern in Python:-
# Output:
# A
# A B
# A B C
# A B C D
# A B C D E

# Solution:-

for i in range(65, 70):
    for j in range(65, i+1):
        print(chr(j), end=" ")
    print()

