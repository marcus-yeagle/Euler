# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.
#
# Marcus Yeagle - marcusnyeagle@gmail.com

a, b = 0, 1
sum = 0

while a < 4000000:
	if a%2 == 0:
		sum+=a
	
	a, b = b, a + b 

print(sum)
