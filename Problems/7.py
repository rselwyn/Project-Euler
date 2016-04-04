import math

def isPrime(num):
    if num==2 or num==3:
        return True
    for i in range(2, (1+math.ceil(math.sqrt(num)))):
        if num%i==0:
            return False
    return True

arr = []
counter = 0
num = 2
while counter<10001:
    if isPrime(num):
        counter+=1
        arr.append(num)
    num+=1

print(arr[len(arr)-1])

## SOLUTION: 104743
