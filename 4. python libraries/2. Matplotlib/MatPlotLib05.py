# using figure and subplots methods-

import warnings
warnings.filterwarnings(action="ignore")

import matplotlib.pyplot as plt

plt.figure(1, figsize=(5, 5))          # it is used to create a new figure
plt.subplot(311)
plt.plot([1, 2, 3])

plt.subplot(312)
plt.plot([4, 5, 6])

plt.subplot(313)
plt.plot([7, 8, 9])
plt.show()

plt.figure(2)
plt.plot([2, 9, 16])
plt.show()

plt.figure(4)
plt.subplot(312)
plt.title("subplot - 312", color='r', fontsize=14, fontweight='bold')
plt.plot([9, 19, 29], [2, 9, 16])

# to create all figures by using 1 show cmd-
plt.show()
