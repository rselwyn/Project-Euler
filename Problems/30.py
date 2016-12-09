def fifth_power_of_digits(n):
	return n == sum([int(i)**5 for i in list(str(n))])

point = 2
while True:
	if fifth_power_of_digits(point):
		print point
	point+=1

# prints
# 4150
#4151
#54748
#92727
#93084
#194979