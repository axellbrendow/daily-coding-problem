def get_palindrome_with_fewest_number_of_insertions(s):
	n = len(s)
	dp = [[''] * n for _ in range(n)]  # dp[i,j] stands for the minimum palindrome between index i and j

	for i in range(n): dp[i][i] = s[i]

	for j in range(n):
		for i in range(j-1,-1,-1):
			if s[i] == s[j]:
				dp[i][j] = s[i] + dp[i+1][j-1] + s[i]
			else:
				insert_right = s[i] + dp[i+1][j] + s[i]
				insert_left = s[j] + dp[i][j-1] + s[j]
				if len(insert_right) < len(insert_left):
					dp[i][j] = insert_right
				elif len(insert_left) < len(insert_right):
					dp[i][j] = insert_left
				else:
					dp[i][j] = insert_left if insert_left < insert_right else insert_right
	return dp[0][n-1]

assert get_palindrome_with_fewest_number_of_insertions('a') == 'a'
assert get_palindrome_with_fewest_number_of_insertions('ac') == 'aca'
assert get_palindrome_with_fewest_number_of_insertions('ca') == 'aca'
assert get_palindrome_with_fewest_number_of_insertions('aac') == 'caac'
assert get_palindrome_with_fewest_number_of_insertions('aace') == 'ecaace'
