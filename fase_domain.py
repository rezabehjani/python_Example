import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

t = np.arange(0, 10.5, step=0.5)
time_serie = np.exp(-t)

plt.figure()
plt.stem(t, time_serie)
plt.grid(True)
plt.xticks([2, 4, 6, 8, 10],
           ["۲", "۴", "۶", "۸", "۱۰"])
plt.show()
