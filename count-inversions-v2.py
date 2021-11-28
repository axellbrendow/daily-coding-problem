def merge(left_result, right_result):
    i, j, count = 0, 0, 0
    result = []
    while i < len(left_result) and j < len(right_result):
        if left_result[i] <= right_result[j]:
            result.append(left_result[i])
            i += 1
        else:
            result.append(right_result[j])
            j += 1
            count += len(left_result) - i
    result += left_result[i:]
    result += right_result[j:]
    return result, count

def mergesort(arr, left, right):
    if left > right: return [], 0
    if left == right: return [arr[left]], 0
    mid = (left + right) // 2
    left_result, left_count = mergesort(arr, left, mid)
    right_result, right_count = mergesort(arr, mid + 1, right)
    merge_result, merge_count = merge(left_result, right_result)
    return merge_result, left_count + right_count + merge_count

def count_inversions(arr):
    return mergesort(arr, 0, len(arr) - 1)[1]

arr = [1, 2, 3, 4, 5]
output = 0
assert count_inversions(arr) == output

arr = [2, 4, 1, 3, 5]
output = 3
assert count_inversions(arr) == output

arr = [5, 4, 3, 2, 1]
output = 10
assert count_inversions(arr) == output
