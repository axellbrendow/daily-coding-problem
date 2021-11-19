def find(character, start, characters):
	indices = []
	for i in range(start, len(characters)):
		if characters[i] == character: indices.append(i)
	return indices

def swap_letters(start, positions, characters):
	for i, pos in zip(range(start, start + len(positions)), positions):
		characters[i], characters[pos] = characters[pos], characters[i]

def segregate(characters):
	pos = 0

	positions = find('R', pos, characters)
	swap_letters(pos, positions, characters)
	pos += len(positions)

	positions = find('G', pos, characters)
	swap_letters(pos, positions, characters)
	pos += len(positions)

characters = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
output = ['R', 'R', 'R', 'G', 'G', 'B', 'B']
segregate(characters)
assert str(characters) == str(output)
