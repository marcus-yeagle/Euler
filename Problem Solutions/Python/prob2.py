# Sum all even Fibonacci Numbers less than 4 Million 
s, x, y = 0, 0, 1
while x < 4000000:
	x, y = y, x+y
	if (x%2 == 0):
		s += x

print(s)
