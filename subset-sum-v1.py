def find_subset_that_adds_up_to_k(nums, target):
	subset = []
	visited = [False] * len(nums)

	def dfs(pos, curr_sum):
		if curr_sum > target: return False
		subset.append(nums[pos])
		if curr_sum == target:
			return True
		visited[pos] = True
		for i, num in enumerate(nums):
			if visited[i]: continue
			if dfs(i, curr_sum + num): return True
		visited[pos] = False
		subset.pop()

	for i, num in enumerate(nums):
		if dfs(i, num): return subset
	return None

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
