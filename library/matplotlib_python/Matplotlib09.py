# creating 2 trignometric graphs into one figure-
# customizing matplotlib graphics - changing the color & linewidth:-

# steps of using func.-
# 1) figure( figsize, dpi)
# 2) xlim / ylim   ==   axis
# 3) xticks / yticks
# 4) xlabel / ylabel
# 5) plot
# 6) title / grid / legend / annotate
# 7) show


import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6), dpi=130)

# create list by using linspace method-
a = np.linspace(-np.pi, np.pi, 250, endpoint=True)
b = np.linspace(-np.pi, np.pi, 250, endpoint=True)

# to set x-limit & y-limit :-
plt.xlim(-3, 4)
plt.ylim(-2, 2)

# to set x-ticks & y-ticks :-
# plt.xticks(a)
# plt.yticks(b)
# we can also do in this way-
plt.xticks(np.linspace(-3, 4, 9, endpoint=True))
plt.yticks(np.linspace(-2, 2, 9, endpoint=True))

# now, plotting is done
plt.xlabel("<------------x cordinates------------->", fontsize=14, color="m")
plt.ylabel("<------------y cordinates------------->", fontsize=14, color="g")
plt.title("Trignometric functions", color="r", fontsize=14)
plt.plot(a, np.sin(a), linewidth=2.0, linestyle="-.", label="sin curve")
plt.plot(b, np.cos(b), linewidth=2.0, linestyle="--", label="cos curve")
plt.legend(loc="upper right")

plt.grid(True)

# show result on screen:-
plt.show()
