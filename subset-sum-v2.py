# dp[i][j] means the subset between 0...i that sum up to j
# The subsets store the indices instead of the values
def find_subset_that_adds_up_to_k(nums, target):
	dp = [[None] * (target + 1) for _ in range(len(nums) + 1)]

	for i in range(len(nums) + 1):
		dp[i][0] = set()

	for curr_target in range(1, target + 1):
		for i in range(len(nums)):
			if i - 1 >= 0:
				dp[i][curr_target] = dp[i - 1][curr_target]
			if curr_target - nums[i] >= 0:
				prev_solution = dp[i - 1][curr_target - nums[i]]
				if prev_solution is not None:
					dp[i][curr_target] = prev_solution | set([i])

	output = dp[len(nums) - 1][target]
	return None if output is None else [nums[i] for i in output]

nums = [1, 2, 3, 4]
target = 10
output = [1, 2, 3, 4]
assert sorted(find_subset_that_adds_up_to_k(nums, target)) == sorted(output)

nums = [12, 1, 61, 5, 9, 2]
target = 24
output = [12, 1, 9, 2]
assert sorted(find_subset_that_adds_up_to_k(nums, target)) == sorted(output)

nums = [12, 1, 61, 5, 9, 2]
target = 1000
output = None
assert find_subset_that_adds_up_to_k(nums, target) == output
