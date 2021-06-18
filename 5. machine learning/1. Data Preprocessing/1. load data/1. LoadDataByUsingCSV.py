# it is old method to use csv library to load data

import csv

filename = open("indians-diabetes.data.csv", 'r')
reader = csv.reader(filename, delimiter=",")
lines = list(reader)

print("total units/lines-", len(lines), '\n\n')

for i in lines:
    print(i)

