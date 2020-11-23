# Developed By : Rishabh Gupta

# Question is- : Write a Python program to read a file line by line store it into an array.

filename = "Dataset.txt"
lst = []

with open(filename, 'r') as fl:
    line = fl.readline()
    count = 1

    while line:
        print("Line {}:- {}".format(count, line.strip()))
        lst.append(line.expandtabs(4).split("\n")[0])
        count += 1
        line = fl.readline()


print("\nno of lines in a file -", count-1)
fl.close()
