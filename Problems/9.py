pairs = []

for a in range(1,1000):
	for b in range(a,1000-a):
		pairs.append([a,b,1000-a-b])

for i in pairs:
	if i[0]**2 + i[1]**2 == i[2]**2:
		print i

# Prints [200,375,425]

print 200*375*425

# 31875000