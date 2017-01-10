# Generate Fibo. 
s, x , y = 0, 1, 2
fibs = [x, y]
for i in xrange(4000000):
	s = x + y
	print s
	x = y
	y = s
	if (s%2 == 0): 
		fibs.append(s) 
del fibs[1]
print (sum(fibs))
