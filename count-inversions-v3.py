def update_fenwick(fenwick, index, delta):
    while index < len(fenwick):
        fenwick[index] += delta
        index += index & -index

def read_fenwick(fenwick, index):
    total = 0
    while index > 0:
        total += fenwick[index]
        index -= index & -index
    return total

def count_inversions(arr):
    nums_and_index = [(num, index + 1) for index, num in enumerate(arr)]
    nums_and_index.sort()
    fenwick = [0 for _ in range(len(arr) + 1)]
    update_fenwick(fenwick, 1, 1)
    update_fenwick(fenwick, nums_and_index[0][1], -1)
    count = 0
    for i in range(1, len(arr)):
        # Get number of values that are less than the current value but are on the right
        # The values on the left will not be counted as there will be -1's on the fenwick tree for them
        count += read_fenwick(fenwick, nums_and_index[i][1])
        update_fenwick(fenwick, 1, 1)
        # As nums_and_index is sorted by value, put -1 on the current index so that the
        # next greater values that appear after this index will not count the current value
        update_fenwick(fenwick, nums_and_index[i][1], -1)
    return count

arr = [1, 2, 3, 4, 5]
output = 0
assert count_inversions(arr) == output

arr = [2, 4, 1, 3, 5]
output = 3
assert count_inversions(arr) == output

arr = [5, 4, 3, 2, 1]
output = 10
assert count_inversions(arr) == output
