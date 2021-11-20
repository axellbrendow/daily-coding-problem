def min_steps(start, end, board):  # start = (0, 2), end = (1, 3)
	lines = len(board)  # 4
	columns = len(board[0])  # 4
	directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
	visited = [[False for _ in range(columns)] for _ in range(lines)]
	def dfs(i, j):  # i = 0, j = 2  |  i = 0, j = 1
		if (
			i < 0 or i >= lines
			or j < 0 or j >= columns
			or visited[i][j]
			or board[i][j]
		): return float('inf')

		if i == end[0] and j == end[1]: return 0

		visited[i][j] = True
		min_steps = float('inf')

		for direction in directions:  # direction = (0, -1)
			steps = dfs(i + direction[0], j + direction[1])
			if steps != float('inf'):
				min_steps = min(min_steps, steps + 1)
		visited[i][j] = False
		return min_steps

	steps = dfs(start[0], start[1])
	return steps if steps != float('inf') else None

board = [
    [True, False, False, True],
    [False, False, True, False],
    [True, False, False, False],
    [True, True, True, True],
]
assert min_steps((0, 2), (1, 3), board) == 6

board = [
    [False, False, False, False],
    [False, False, True, False],
    [True, False, False, False],
    [True, True, True, True],
]
assert min_steps((0, 1), (0, 0), board) == 1

board = [
	[False,	False,	False,	False,	False],
	[False,	True,	False,	True,	False],
	[False,	True,	False,	True,	False],
	[False,	True,	True,	True,	False],
	[False,	False,	False,	False,	False],
]
start = (4, 0)
dest = (2, 2)
assert min_steps(start, dest, board) == 8
