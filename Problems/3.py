arr = []
for i in range(100,1000):
    for b in range(100,1000):
        if (str(i*b) == str(i*b)[::-1]):
            arr.append(i*b)

arr = sorted(arr)
print(arr[len(arr)-1])


##SOLUTION: 906609
