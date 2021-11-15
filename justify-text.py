def distribute_spaces_evenly(start, end, curr_len, words, k):
	num_blocks = (end - start)
	if num_blocks == 0:
		return words[start] + (' ' * (k - curr_len))

	remaining_spaces = k - curr_len + num_blocks
	num_spaces_foreach_block = remaining_spaces // num_blocks
	extra_spaces = remaining_spaces % num_blocks
	line = words[start]
	for i in range(start + 1, end + 1):
		spaces = ' ' * (num_spaces_foreach_block + (0 if extra_spaces == 0 else 1))
		if extra_spaces > 0: extra_spaces -= 1
		line += f'{spaces}{words[i]}'
	return line

def justify_text(words, k):
	start = 0
	end = 0
	curr_len = len(words[0])
	output = []
	for i in range(1, len(words)):
		if curr_len + len(words[i]) + 1 > k:
			output.append(distribute_spaces_evenly(start, end, curr_len, words, k))
			start = end = i
			curr_len = len(words[i])
		else:
			end = i
			curr_len += len(words[i]) + 1
	output.append(distribute_spaces_evenly(start, end, curr_len, words, k))
	return output

assert str(justify_text(["abc", "bc", "a"], 7)) == str(['abc  bc', 'a      '])
