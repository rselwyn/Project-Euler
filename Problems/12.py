def factors(n):
    return reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))
numToAdd = 2
currentSum = 1
while len(factors(currentSum)) < 500:
	currentSum += numToAdd
	numToAdd+=1
print currentSum # 76576500
