#Fibonacci

x1 = 1
x2 = 2
x3 = 0
xmax = 1000000
sum_impar = 1 #el primer impar es x1=1

while x3 < xmax:
  x3 = x1 + x2
  if x3%2!=0 and x3<xmax :
    sum_impar = sum_impar + x3
  x1 = x2
  x2 = x3
print sum_impar
