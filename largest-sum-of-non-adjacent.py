def largest_sum_of_non_adjacent1(integers):
	cache = {}

	def largest_sum_of_non_adjacent_rec(index):
		if index in cache:
			return cache[index]

		if index >= len(integers):
			return 0

		no_pick_sum = largest_sum_of_non_adjacent_rec(index + 1)
		pick_sum = integers[index] + largest_sum_of_non_adjacent_rec(index + 2)

		max_sum = max(no_pick_sum, pick_sum)
		cache[index] = max_sum
		return max_sum

	return largest_sum_of_non_adjacent_rec(0)


def largest_sum_of_non_adjacent2(integers):
    if len(integers) == 0: return 0

    no_pick_sum = 0
    pick_sum = integers[-1]

    for i in range(len(integers) - 2, -1, -1):
        temp = no_pick_sum
        no_pick_sum = max(no_pick_sum, pick_sum)
        pick_sum = integers[i] + temp

    return max(no_pick_sum, pick_sum)


assert largest_sum_of_non_adjacent1([]) == 0
assert largest_sum_of_non_adjacent1([1]) == 1
assert largest_sum_of_non_adjacent1([1, 2]) == 2
assert largest_sum_of_non_adjacent1([1, 2, 3]) == 4
assert largest_sum_of_non_adjacent1([5, 1, 1, 5]) == 10

assert largest_sum_of_non_adjacent2([]) == 0
assert largest_sum_of_non_adjacent2([1]) == 1
assert largest_sum_of_non_adjacent2([1, 2]) == 2
assert largest_sum_of_non_adjacent2([1, 2, 3]) == 4
assert largest_sum_of_non_adjacent2([5, 1, 1, 5]) == 10
