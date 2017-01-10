# Find the difference between the sum of the squares of the first 100 N and the # square of the sum.
#
# Marcus Yeagle - marcus.yeagle@gmail.com

def find_sum_of_squares(k):
	m = k + 1
	n = 2 * k
	o = n + 1

	numer = k * m
	numer = numer * o

	sum = numer / 6
	
	return sum



def square_of_the_sum(n):
	m = n + 1
	numer = n * m

	sum = numer / 2

	return sum*sum


print (square_of_the_sum(100)- find_sum_of_squares(100))
