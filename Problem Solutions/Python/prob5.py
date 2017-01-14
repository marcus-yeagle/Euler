# Finds the smallest positive number that is evenly divisible 
# by all of the numbers from 1 to 20

def find_min_div():
	n = 2520
	while (True):
		flg = True
		for x in range(20,10,-1):
			print('Is %d div. by %d ?' % (n, x))
			if (n % x != 0):
				flg = False
				break
		if (flg):
			return n
		else:
			n += 2

print (find_min_div())
