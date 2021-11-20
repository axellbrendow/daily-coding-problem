def generate_power_set(nums):  # This solution does not generate the sets ordered by the length
	num_sets = 1 << len(nums)
	sets = [[] for _ in range(num_sets)]
	for i in range(num_sets):
		for j in range(len(nums)):
			if (i >> j) & 1:
				sets[i].append(nums[j])
	return sets

nums = [1, 2, 3]
output = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
assert str(sorted(generate_power_set(nums))) == str(sorted(output))
