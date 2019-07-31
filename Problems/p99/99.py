import math

f = [i.split(",") for i in open("p099_base_exp.txt","r").readlines()]
print f
largest_line = -1
largest_num = 0
for num,i in enumerate(f):
    val = float(i[1]) * math.log(float(i[0]))
    if val > largest_num:
        largest_num = val
        largest_line = num

print largest_line + 1
# Because it starts at 0

# 709

