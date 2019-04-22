import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
j=np.complex(0,1)
N=1000
t=np.linspace(0,1,N,endpoint=False)
x1=signal.square(2 * np.pi * 5 * t)
x2=x1
a=len(x1)
a1=len(x2)
y=np.zeros(a+a1-1)
for i in range(0,N):
	for k in range(0,a):
		if((i-k)>=0 and (i-k)<=2):
			y[i]=y[i]+(x1[k]*x2[i-k])
plt.subplot(311)
plt.plot(t,x1)
plt.subplot(312)
plt.plot(t,x2)
plt.subplot(313)
plt.plot(y)
plt.show()
print(y)
