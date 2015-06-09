# Find the 10,001st prime number.
#
# Marcus Yeagle - marcus.yeagle@gmail.com

def is_prime(n, primes):
	for p in primes:
		if n % p == 0:
			#Number is composite
			return
		
	primes.append(n)

	
primes = [2]
i = 3 

while len(primes) != 10001:
	is_prime(i, primes)
	i += 1

	
print (primes[10000])