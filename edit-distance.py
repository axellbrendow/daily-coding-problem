def min_edit_distance(source, target):
	def dfs(string, index_string, index_target, num_edits):
		if index_string >= len(string):
			return num_edits + len(target) - index_target

		if index_target >= len(target):
			return num_edits + len(string) - index_string

		min_edits = float('inf')
		if string[index_string] == target[index_target]:
			min_edits = dfs(string, index_string + 1, index_target + 1, num_edits)
		else:
			char_removed = string[:index_string] + string[index_string + 1:]
			min_edits = min(min_edits, dfs(char_removed, index_string, index_target, num_edits + 1))

			char_inserted = string[:index_string] + target[index_target] + string[index_string:]
			min_edits = min(min_edits, dfs(char_inserted, index_string + 1, index_target + 1, num_edits + 1))

			char_replaced = string[:index_string] + target[index_target] + string[index_string + 1:]
			min_edits = min(min_edits, dfs(char_replaced, index_target + 1, index_target + 1, num_edits + 1))
		return min_edits

	return dfs(source, 0, 0, 0)

assert min_edit_distance('horse', 'ros') == 3
assert min_edit_distance('kitten', 'sitting') == 3
