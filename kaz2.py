from matplotlib import pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

array = [5.165,
5.717,
5.478,
4.640,
4.286,
3.777,
4.367,
4.737,
4.518,
5.068,
4.713,
4.130,
4.903,
4.326,
4.687,
3.688,
4.466,
4.668,
4.517,
3.723,
4.520,
4.129,
4.336,
4.143,
4.662,
3.879,
4.541,
4.235,
4.478,
4.703
]
n, bins, patches = plt.hist(array, 50, normed=1)
mu = np.mean(array)
sigma = np.std(array)
plt.plot(bins, mlab.normpdf(bins, mu, sigma))