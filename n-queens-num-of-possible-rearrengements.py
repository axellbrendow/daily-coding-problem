def safe_to_place_queen_at(line, col, N, queens):
	for i in range(line - 1, -1, -1):
		if (i, col) in queens: return False

	i, j = line, col
	while i >= 0 and j >= 0:
		if (i, j) in queens: return False
		i -= 1
		j -= 1

	i, j = line, col
	while i >= 0 and j < N:
		if (i, j) in queens: return False
		i -= 1
		j += 1

	return True

def find_num_of_rearrangements(N):
	queens = set()
	def dfs(row, num_queens):
		if num_queens == N: return 1
		num_of_rearrangements = 0
		for col in range(N):
			if safe_to_place_queen_at(row, col, N, queens):
				queens.add((row, col))
				num_of_rearrangements += dfs(row + 1, num_queens + 1)
				queens.remove((row, col))
		return num_of_rearrangements
	return dfs(0, 0)

N = 1
assert find_num_of_rearrangements(N) == 1

N = 2
assert find_num_of_rearrangements(N) == 0

N = 3
assert find_num_of_rearrangements(N) == 0

N = 4
assert find_num_of_rearrangements(N) == 2

N = 8
assert find_num_of_rearrangements(N) == 92
