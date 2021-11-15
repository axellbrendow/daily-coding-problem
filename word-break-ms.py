def insert_trie(root, word):  # word = 'abc'
	for letter in word:  # 'c'
		if not letter in root:
			root[letter] = {}
		root = root[letter]
	root['$'] = {}

def build_trie(words_set):
	trie = {}
	for word in words_set:
		insert_trie(trie, word)
	return trie

def get_sentence_list(s, words_set):
	if len(s) == 0: return []

	trie = build_trie(words_set)
	output = []

	def dfs(i, node, prefix):
		if i >= len(s):
			output.append(prefix)
			return True
		for child in node:
			if child == '$':
				output.append(prefix)
				if dfs(i, trie, ''): return True
				output.pop()
			if s[i] == child:
				if dfs(i + 1, node[child], prefix + child): return True
		return False

	return output if dfs(0, trie, '') else None

assert str(get_sentence_list('thequickbrownfox', ['the', 'quick', 'brown', 'fox'])) \
	== str(['the', 'quick', 'brown', 'fox'])
