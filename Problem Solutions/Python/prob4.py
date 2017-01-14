# Find the largest palindrome made from the product
# of two 3-digit numbers

def find_pal():
	pals = []
	for x in range(999,99,-1):
		for y in range(999,99,-1):
			p = str(x*y)
			if (p == p[::-1]):
				pals.append(int(p))

	return max(pals)

print(find_pal())
