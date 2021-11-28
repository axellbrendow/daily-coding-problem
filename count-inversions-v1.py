def insert_sorted(num, sorted_arr):
    if len(sorted_arr) == 0:
        sorted_arr.append(num)
        return 0

    left, right = 0, len(sorted_arr) - 1
    mid = (left + right) // 2

    while left <= right:
        mid = (left + right) // 2
        if num == sorted_arr[mid]: break
        elif num < sorted_arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if num <= sorted_arr[mid]:
        sorted_arr.insert(mid, num)
        return mid

    else:
        sorted_arr.insert(mid + 1, num)
        return mid + 1

def count_inversions(arr):
    inversions = 0
    sorted_arr = []
    for num in arr:
        index = insert_sorted(num, sorted_arr)
        inversions += len(sorted_arr) - index - 1
    return inversions

arr = [2, 4, 1, 3, 5]
output = 3
assert count_inversions(arr) == output
