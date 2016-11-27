def perform_collatz(start):
	iterations = 0
	while start != 1:
		if start%2==0:
			start/=2
		else:
			start = start*3 + 1

		iterations+=1

	return iterations

max_chain = -1
accompanying_max_chain_number = -1

for i in range(2, 1000000):
	num = perform_collatz(i)
	print i # status indicator
	if num > max_chain:
		print num
		max_chain = num
		accompanying_max_chain_number = i

print accompanying_max_chain_number
# 837799