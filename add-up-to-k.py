'''
15-10-2021

https://docs.google.com/document/d/18kkJ9b8gRS0KlhaDCZ2CnqfTLUHRo_h7YxXpZKEmpA8/edit?usp=sharing

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

1 - the list fit in memory
2 - all numbers fit in memory
3 - all numbers can be negative
4 - list can be empty
5 - you can have duplicates
6 - the number are integers, not floats

def check_sum(arr, k):
	nums_set = set()
	for num in arr: # O(n)
		if (k - num) in nums_set: # O(1)
			return True
		nums_set.add(num) # O(1)
	return False

Testing:

check_sum {
	arr = [10, 15, 3, 7]
	k = 17
	nums_set = set(10, 15, 3)
	num = 7
	return True
}

check_sum {
	arr = []
	k = 17
	nums_set = set()
	return False
}

check_sum {
	arr = [-1, 2, -5, 6]
	k = -6
	nums_set = set(-1, 2)
	num = -5
	return True
}


check_sum {
	arr = [5, 5, 3, 2]
	k = 10
	nums_set = set(5, )
	num = 5
}

Time and space complexity:

time = O(n)
space = O(n)
'''
