def find_max_profit(prices):
	stack = []
	max_profit = 0
	for i in range(len(prices)):
		while len(stack) > 0 and prices[stack[-1]] >= prices[i]:
			stack.pop()
		if len(stack) > 0:
			max_profit = max(max_profit, prices[i] - prices[stack[0]])
		stack.append(i)
	return max_profit

prices = []
output = 0
assert find_max_profit(prices) == output

prices = [1]
output = 0
assert find_max_profit(prices) == output

prices = [1, 1]
output = 0
assert find_max_profit(prices) == output

prices = [1, 0]
output = 0
assert find_max_profit(prices) == output

prices = [1, 2]
output = 1
assert find_max_profit(prices) == output

prices = [1, 5, 10, 2, 100]
output = 99
assert find_max_profit(prices) == output
