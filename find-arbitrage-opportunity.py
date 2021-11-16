def is_arbitrage_possible(exchange_rates):
	visited = [False] * len(exchange_rates)
	curr_visited = [False] * len(exchange_rates)

	def dfs(node, weight):
		if visited[node]: return False
		if curr_visited[node]:
			return weight > 1
		curr_visited[node] = True
		for i in range(len(exchange_rates)):
			if i == node: continue
			if dfs(i, weight * exchange_rates[node][i]):
				return True
		curr_visited[node] = False
		visited[node] = True
		return False

	return dfs(0, 1)

assert is_arbitrage_possible([
	[1.0, 2.0, 5.0],
	[0.5, 1.0, 3.0],
	[0.2, 0.33, 1.0],
]) == True
