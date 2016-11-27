import inflect

eng = inflect.engine()

numbers = 0

for i in range(1,1001):
	letters = eng.number_to_words(i)
	letters = "".join("".join(letters.split(" ")).split("-"))
	# print letters
	numbers += len(letters)

print numbers
# 21124