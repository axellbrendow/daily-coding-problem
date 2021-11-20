def generate_power_set(nums):
	output = []
	subset = []

	def gen(start, length):
		if start + length > len(nums): return
		if length <= 0:
			output.append(subset.copy())
			return

		for i in range(start, len(nums)):
			subset.append(nums[i])
			gen(i + 1, length - 1)
			subset.pop()

	for length in range(len(nums)+1):
		gen(0, length)

	return output

nums = [1, 2, 3]
output = [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
assert str(generate_power_set(nums)) == str(output)
