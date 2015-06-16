# This is a re-factorization of the C++ solution of finding 
# the largest palindrome of a 3 digit product.
#
# Marcus Yeagle - marcus.yeagle@gmail.com

largest = 0

for i in range(100,1000):
	for j in range(100,1000):
		prod = i*j
		prod = str(prod)
		reversed = prod[::-1]
		if prod == reversed:
			prod = int(prod)
			if prod > largest:
				largest = prod
				
print (largest)
