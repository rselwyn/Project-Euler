hundred = list(range(1,101))

sum_of_squares = sum([i**2 for i in hundred])

square_of_sum = sum([i for i in hundred])**2

print((-sum_of_squares + square_of_sum))

## ANSWER: 25164150
