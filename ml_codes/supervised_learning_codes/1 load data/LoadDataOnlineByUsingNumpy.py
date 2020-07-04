# to load data online by using numpy-

import numpy as np
import urllib.request

web_path = urllib.request.urlopen("https://goo.gl/QnHW4g")

# to read data
dataset = np.genfromtxt(web_path, delimiter=",")

print(dataset, '\n\n')

for i in dataset:
    print(i)

print(dataset.shape)
