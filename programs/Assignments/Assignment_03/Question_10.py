# Developed By : Rishabh Gupta

# Question is-  Write a Python program to count the number of lines in a text file.

filename = "Dataset.txt"
no_of_lines = 0

with open(filename, 'r') as f1:
    for line in f1:
        no_of_lines += 1
print("no of lines in a file--", no_of_lines)
