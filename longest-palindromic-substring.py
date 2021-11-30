def find_longest_palindromic_contiguous_substr(string):
	if len(string) <= 1: return string
	longest = ''
	dp = [[False] * (len(string) + 1) for _ in range(len(string))]
	for i in range(len(dp)):
		dp[i][0] = True
		dp[i][1] = True
	for length in range(2, len(string) + 1):
		for i in range(len(string) - length + 1):
			end = i + length - 1
			if dp[i + 1][length - 2] and string[i] == string[end]:
				dp[i][length] = True
				if length > len(longest):
					longest = string[i:i + length]
	return longest

string = ''
output = ''
assert find_longest_palindromic_contiguous_substr(string) == output

string = 'a'
output = 'a'
assert find_longest_palindromic_contiguous_substr(string) == output

string = 'ab'
output = ''
assert find_longest_palindromic_contiguous_substr(string) == output

string = 'aa'
output = 'aa'
assert find_longest_palindromic_contiguous_substr(string) == output

string = 'aba'
output = 'aba'
assert find_longest_palindromic_contiguous_substr(string) == output

string = 'abb'
output = 'bb'
assert find_longest_palindromic_contiguous_substr(string) == output
