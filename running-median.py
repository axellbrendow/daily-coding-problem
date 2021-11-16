def get_insertion_pos(value, arr):  # value = 1, arr = [2]
	left = 0  # 0
	right = len(arr) - 1  # 0
	mid = (left + right) // 2  # 0
	while left < right:
		if value == mid: return mid
		elif value < mid:
			right = mid - 1
		else:
			left = mid + 1
		mid = (left + right) // 2
	return mid if len(arr) == 0 or value <= arr[mid] else mid + 1  # 0

def get_median(arr):  # arr = [1, 2]
	n = len(arr)  # 2
	middle = n // 2  # 1
	if n % 2 == 1:
		return arr[middle]  # 2
	else:
		return ( arr[middle - 1] + arr[middle] ) / 2  # (arr[0] + arr[1]) / 2 = 1.5

def get_running_median(sequence):  # [2, 1, 5, 7, 2, 0, 5]
	sorted_sequence = []  # [1, 2]
	for value in sequence:  # value = 1
		pos = get_insertion_pos(value, sorted_sequence)  # 0
		sorted_sequence.insert(pos, value)  # 0, 1
		yield get_median(sorted_sequence)  # 2, 1.5

sequence = [2, 1, 5, 7, 2, 0, 5]
output = [2, 1.5, 2, 3.5, 2, 2, 2]
for median, expected in zip(get_running_median(sequence), output):
    assert median == expected
