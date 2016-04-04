
def isDivisible(num):
    return not False in [num%i==0 for i in range(2,21)]

#Num is 19*17*15*13*4*7*11
num = 19399380
while not isDivisible(num):
    num+=19399380
print(num)

## ANSWER: 232792560
