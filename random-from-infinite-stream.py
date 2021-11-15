import random

def random_from_stream(stream):
	res = stream[0]
	i = 1
	while i < len(stream):
		rand = random.randrange(i + 1)
		if rand == i:
			res = stream[i]
		i += 1
	return res

assert random_from_stream([0]) == 0
print()
print(random_from_stream([0, 1]))
print(random_from_stream([0, 1]))
print(random_from_stream([0, 1]))
print(random_from_stream([0, 1]))
print(random_from_stream([0, 1]))
print()
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(random_from_stream([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
