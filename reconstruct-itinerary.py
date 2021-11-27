from collections import defaultdict

def build_graph(flights):
	flights.sort()
	graph = defaultdict(list)
	for src, dest in flights:
		graph[src].append(dest)
		if not dest in graph:
			graph[dest] = []
	return graph

def find_eulerian_path(graph, flights, start):
	path = []
	visited = defaultdict(int)
	for src, dest in flights:
		visited[(src, dest)] += 1
	def dfs(node):
		for child in graph[node]:
			if visited[(node, child)] == 0: continue
			visited[(node, child)] -= 1
			dfs(child)
		path.append(node)
	dfs(start)
	return None if len(path) != len(flights) + 1 else path[::-1]

def find_lexicographically_smallest_itenerary(flights, start):
	graph = build_graph(flights)
	return find_eulerian_path(graph, flights, start)

flights = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
start = 'JFK'
output = ["JFK","NRT","JFK","KUL"]
assert find_lexicographically_smallest_itenerary(flights, start) == output

flights = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
start = 'KUL'
output = None
assert find_lexicographically_smallest_itenerary(flights, start) == output

flights = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
start = 'JFK'
output = ["JFK","MUC","LHR","SFO","SJC"]
assert find_lexicographically_smallest_itenerary(flights, start) == output

flights = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]]
start = 'JFK'
output = ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]
assert find_lexicographically_smallest_itenerary(flights, start) == output
