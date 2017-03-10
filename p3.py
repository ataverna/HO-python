import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

data = open("salida_p3.dat",'w')

x = np.linspace(-10,10,100)
coef = [1,1,-4,4]
y = np.poly1d(coef)
xx = np.linspace(-10,10,201)

#derivada
dy = derivative(y,x,dx=1e-6)

np.savetxt(data,y(xx),fmt='%f',delimiter='\t',header='x #f(x)')
data.close()

plt.plot(x,y(x),'b-',label='Polinomio')
plt.plot(x,dy,'r-',label='Derivada')
plt.plot(xx,y(xx),'go',label='cada 0.1 pasos',markersize=1)
legend = plt.legend(loc='upper left',shadow=False,fontsize=10)
plt.xlabel('X')
plt.ylabel('f(X)')
plt.xlim([-10,10])
plt.grid(True)

plt.show()

