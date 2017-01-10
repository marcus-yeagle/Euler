# Largest prime factor
def largest_p_fact(n):
	factors = []
	div = 2
	while n > 1:
		if n % div == 0:
			factors.append(div)
			n = n / div
		div = div + 1

	return max(factors)

print (largest_p_fact(600851475143))
