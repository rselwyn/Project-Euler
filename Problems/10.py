import math

def isPrime(value):
	for i in range(2,int(math.floor(math.sqrt(value))) + 1):
		if value%i==0:
			return False
	return True

# Total of primes
total = 0

# Current primes to look at it
currentPoint = 2

while currentPoint < 2000000:
	if isPrime(currentPoint):
		total += currentPoint

	currentPoint += 1

	# Irrelevant but just status updates
	if not currentPoint % 100000:
		print currentPoint

print total 