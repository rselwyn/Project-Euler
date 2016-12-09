f = open("ignore_p22.txt","r")

def get_letter_value(n):
	return sum([int(ord(i)) - 96 for i in n.lower()])

data = [i[1:-1] for i in f.readlines()[0].split(",")]
data = sorted(data)

sumv = 0

for iterv in enumerate(data):
	sumv += (iterv[0]+1) * get_letter_value(iterv[1])

print sumv