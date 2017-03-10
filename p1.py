#x = range(1000)
#print x

sum_x = 0
for x in range(1000):
  if(x%3==0 or x%5==0):
    sum_x = sum_x + x

print sum_x
