
# import matplotlib.pyplot as mp
from matplotlib import pyplot as plt


# plot() fnx - it takes min 2 args (as a list) to represent x & y cordinates-
# 1st arg - act as x-cordinates
# 2nd arg - act as y-cordinates
# Note- if we give only 1 arg then it will be used as y-cordinates & their indexes will become the
# list of x-cordinates in a graph.
#
# plt.plot([1, 2, 3, 4])
# plt.show()      # [1,2,3,4] act as y-cordinates & [0,1,2,3] act as x-cordinates
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.xlabel("-----x value--------")
# plt.ylabel("-----y values--------")
#
# # axis fnx. will take list as arg.- in which first 2 elements out of 4 elements represents the range of x-axis &
# # last 2 elements out of 4 elements represents the range of y-axis--
# plt.axis([0, 5, 0, 16])            # here we see 2 quadrants only due to given range
# plt.show()
#
#
# linewidth defines- thickness of line
# legend- it uses label to give info about the graph/line
# label- tells the name of graph/line
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-.', label="line 1", linewidth=2)
plt.plot([2, 5, 13, 19], [4, 8, 16, 23], 'mo--', label='line 2', linewidth=2)
plt.xlabel("------x cordinates----------")
plt.ylabel("------y cordinates----------")
plt.axis([-0.5, 21, -5, 25])          # here we see all 4 quadrants due to given range
plt.legend(loc='upper right')
plt.show()
























































































































