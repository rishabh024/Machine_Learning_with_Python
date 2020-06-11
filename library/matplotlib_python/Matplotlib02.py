import matplotlib.pyplot as plt

# to create multiple lines by using only one plot cmd-
# for it, we have to supply the positional & keyword argument

x1 = [1, 2, 3]
y1 = [4, 5, 9]
x2 = [2, 3, 4]
y2 = [4, 7, 9]

# note- labels are placed in the legend.
# pattern of arg. in plot is- ( list[x1], list[y1], list[x2], list[y2] ) all  lists represent cordinates.
plt.plot(x1, y1, x2, y2, "mo-.", linewidth=2)
plt.xlabel("---------x cordinates------------")
plt.ylabel("---------y cordinates------------")
plt.legend(loc="upper right")
plt.axis([-0.5, 5, -0.5, 10])
plt.show()

