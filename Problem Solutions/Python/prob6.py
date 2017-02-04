# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.

def diff():
	sum_of_sqs = 0
	sq_of_sums = 0

	for i in range(101):
		sum_of_sqs += (i**2)
		sq_of_sums += i

	return (sq_of_sums ** 2) - sum_of_sqs

print diff()
