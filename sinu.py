import matplotlib.pyplot as plt
import numpy as np
fs=50
f=4
sample=100
a=np.arange(sample)
b=np.sin(2*np.pi*f*a/fs)
plt.plot(a,b)
plt.xlabel('sample(n)')
plt.ylabel('voltage(v)')
plt.show()
