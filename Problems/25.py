data1 = 1
data2 = 1
counter = 2
while True:
	data1, data2 = data2, data1+data2
	counter +=1
        print data1, data2
	#print len(str(data2))
	if len(str(data2)) == 1000:
		print counter
		break

# 4782
# After some more thought to this problem, there is an O(1) solution
# that involves using the closed form for finding fibonacci numbers.  We know that
# 1 + log_10(n) gives the number of digits.  Additionally, there is a closed form for the
# nth fibonacci number.  Using this, an equation can be set up that can be computed in O(1).
