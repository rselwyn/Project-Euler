x = int(0) #accumulator
for i in range(1,1000):
    if i%3==0 or i%5==0:
        x = x + i
print(x)
