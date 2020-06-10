from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]


plt.plot(x, y, marker='o', markerfacecolor="m", markersize=10,
              linestyle='-.', linewidth=2, label="line 1", color='g')

plt.xlabel('<-------------x cordinates------------->', fontsize=14, color="g")
plt.ylabel("<-------------y cordinates------------->", fontsize=14, color="b")
plt.title("numbers with squares",fontsize=15, color="r")
plt.grid(True)
plt.legend(loc="upper right")
plt.annotate("Square of 5", color='c', xytext=(4, 30), xy=(5, 25), arrowprops=dict( facecolor="r", shrink=.08))
plt.axis([0, 7, 0, 37])                # in axis fnx-list is given in this way-[ x1, x2, y1, y2]
plt.show()

