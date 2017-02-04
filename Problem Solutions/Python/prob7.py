# What is the 10 001st prime number?

import math

def is_prime(x):
	i = 2
	while (i <= (math.floor(math.sqrt(x)))):
		if (x % i == 0):
			return False
		i+=1

	return True


def nth_prime(n):
	primes = [2]
	x = 3
	while (len(primes) < n):
		if (is_prime(x)):
			primes.append(x)
		x+=1
	return primes[-1]

print nth_prime(10001)
