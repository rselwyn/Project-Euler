primesUpTo = lambda N: reduce( (lambda r,x: r-set(range(x**2,N,x)) if (x in r) else r), 
        range(2,N), set(range(2,N)))

def works(number, power):
	return (number - 2 * power**2) in fat_primes

fat_primes = set(primesUpTo(10000))
print fat_primes
number = 9
while True:
	print number

	if number in fat_primes:
		number += 2
		continue

	power = 1
	while True:
		print power
		if works(number, power):	
			break
		power += 1
	number += 2