# draw the graphs of trignometric fnxs--

import matplotlib.pyplot as plt
import numpy as np

# plotting with default settings-
a = np.linspace(-np.pi, np.pi, 256, endpoint=True)

# Note:--
# cot fnx - arccos()
# sec fnx - arccos()
# cosec fnx - arcsin()

plt.figure(1)

plt.subplot(321)
plt.title("sin func.", color="r")
plt.legend(loc="upper right")
plt.plot(a, np.sin(a), label="sin func")

plt.subplot(322)
plt.title("cos func.", color="m")
plt.legend(loc="upper right")
plt.plot(a, np.cos(a), label="cos func")

plt.subplot(323)
plt.title("tan func.", color="g")
plt.legend(loc="upper right")
plt.plot(a, np.tan(a), label="tan func")

plt.subplot(324)
plt.title("cot func.", color="b")
plt.legend(loc="upper right")
plt.plot(a, np.arctan(a), label="cot func")

plt.subplot(325)
plt.title("sec func.", color="c")
plt.legend(loc="upper right")
plt.plot(a, np.arccos(a), label="sec func")

plt.subplot(326)
plt.title("cosec func.", color="m")
plt.legend(loc="upper right")
plt.plot(a, np.arcsin(a), label="cosec func")

plt.show()

