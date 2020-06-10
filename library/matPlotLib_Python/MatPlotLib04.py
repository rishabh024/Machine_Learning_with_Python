import numpy as np
import matplotlib.pyplot as plt

# create evenly sampled time at 200ms intervals
t = np.arange(0.0, 5.0, 0.2)
print(t)

# create multiple lines in same graph
# in string format- representation is-- 'color_name/cordinates/line'
# 'red star dashed- 'r*--', blue square solid line - 'bs-', green triangle solid- 'gv-'

# this line is used when we want same color on marker as it is on line. For it, use (x1, y1) 1 time
# plt.plot(t, t, 'r*-', t, t+3, 'bs-', t, t+6, 'gv-.', t, t+4, 'mo:', markersize=7)

# this line is used when we want different color on marker & on line. For it, use (x1, y1) 2 times.
# we can draw in any way- Either-
# a) first draw line then draw marker, or
# b) first draw marker then draw line

plt.plot(t, t, 'g-.',  t, t, 'ro',
         t, t+3, 'b*', t, t+3, 'm--',
         t, t+6, 'cv', t, t+6, 'g-.',
         t, t+4, 'm-', t, t+4, 'ro', markersize=7)

plt.show()
