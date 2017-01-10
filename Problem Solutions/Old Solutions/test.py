tri = []

tri.append([3])
tri.append([7,4])
tri.append([2,4,6])
tri.append([8,5,9,3])
	
for row in range(0,3):
	row_max = max(tri[row])
	row_len = len(tri[row])
	next_row_len = len(tri[row+1])
	
	#Update left edge
	tri[row+1][0] += tri[row][0]
	
	#Update right edge
	#tri[row+1][next_row_len] += tri[row][row_len]
	
	print (tri[row+1][next_row_len])

	
#print (max(tri[row+1]))
	
