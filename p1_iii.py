#factores primos
import math 

x1 = 13195
x2 = 600851475143
xmax = x2/3 + 1

def primos(x):
  xx = math.sqrt(x)
  for i in range(2,int(xx)+1):
    xxx = x%i
    if(xxx==0):
      return False
  return True

for i in range(1,int(x2**0.5)+1):
  if(x2%i==0 and primos(i)):
    print i

print '----otra forma'
for i in range(2,int(x2**0.5)+1):
  if (x2%i==0 and x2!=i):
    x2 /= i
    print x2
  
