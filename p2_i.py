import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dd=np.genfromtxt("tabla.dat",unpack=True)

x = dd [0]
y = dd [1]
#print x 
#print y

coef = np.polyfit(x,y,9)
print coef
pol = np.poly1d(coef)
x1 = np.linspace(4.1,9.17,100)

#plot
plt.plot(x,y,'ro',label='Datos')
plt.plot(x1,pol(x1),'b-',label='Fit')

plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
legend = plt.legend(loc='upper left',shadow=False,fontsize=10)

plt.show()	

###################

#data = np.loadtxt("tabla.dat")
#print type(data)

#como sabe a que valores de y se tiene que acercar???
#def fitFunc(x,a,b,c,d):
#  return a*x**3+b*x**2+c*x+d 
#yy = fitFunc(x,2.5,-1.3,0.5,1)
#noisy = yy + 0.25*np.random.normal(size=len(yy))
#p0 = [2,-1,0.5,1]
#fitParams, matcov = curve_fit(fitFunc,x,y,p0)
#yaj = fitFunc(x,fitParams[0],fitParams[1],fitParams[2],fitParams[3])

#plt.plot(x,yaj,'b-',label='Ajuste')
#print fitParams
#print yaj
