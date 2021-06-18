# creating 2 trignometric graphs into one subplot in one figure-
# customizing matplotlib graphics - changing the color & linewidth

import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(-np.pi, np.pi, 256, endpoint=True)

plt.figure(figsize=(8, 6), dpi=130)

plt.subplot(311)
plt.plot(a, np.sin(a), color='r', linewidth=2.0, linestyle='-.', label="sin curve")
plt.plot(a, np.cos(a), color='g', linewidth=2.0, linestyle='--', label="cos curve")
plt.legend(loc="upper right")

plt.subplot(312)
plt.plot(a, np.tan(a), color='m', linewidth=2.0, linestyle='-', label="tan curve")
plt.plot(a, np.arctan(a), color='c', linewidth=2.0, linestyle='-.', label="cot curve")
plt.legend(loc="upper right")

plt.subplot(313)
plt.plot(a, np.arccos(a), color='b', linewidth=2.0, linestyle='--', label="sec curve")
plt.plot(a, np.arcsin(a), color='m', linewidth=2.0, linestyle='-', label="cosec curve")
plt.legend(loc="upper right")

plt.show()
