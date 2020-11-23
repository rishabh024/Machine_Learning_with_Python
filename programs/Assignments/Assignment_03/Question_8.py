# Developed By : Rishabh Gupta

# Question is-  Write a Python program to read an entire text file.

import pandas as pd

# to read any text file, use pandas in this way--
# file = pd.read_csv("Python_file.txt")
# print("to read entire file-", file)


heading_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
file = pd.read_csv("indians-diabetes.data.csv", names=heading_names)
print("your data file is--\n", file)
