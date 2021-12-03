def find_max_sum_of_any_contiguous_subarray(array):
	curr_sum = 0
	max_sum = 0
	for i in range(len(array)):
		curr_sum = max(0, curr_sum + array[i])
		max_sum = max(max_sum, curr_sum)
	return max_sum

array = [34, -50, 42, 14, -5, 86]
output = 137
assert find_max_sum_of_any_contiguous_subarray(array) == output
