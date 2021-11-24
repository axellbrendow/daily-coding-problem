'''
When a bit 1 is seen by the first time, store it in 'odd'
If a new bit 1 is seen and there's a bit 1 at 'odd', pass this bit to 'even'
If a new bit 1 is seen and there's a bit 1 at 'even', remove that bit

These 3 states always eliminates values that repeats 3 times

As the first state of 'odd' and 'even' is zero, when we set the bits of
'odd' and 'even' to zero we are just returning to the initial state.

num     odd     even  |  new_odd    new_even
0       0       0     |  0          0
0       1       0     |  1          0
0       0       1     |  0          1
1       0       0     |  1          0
1       1       0     |  0          1
1       0       1     |  0          0

new_odd minterms
    = (~num . odd . ~even) + (num . ~odd . ~even)
    = (~num . odd + num . ~odd) . ~even
    = (num xor odd) . ~even

new_even minterms
    = (~num . even . ~new_odd) + (num . ~even . ~new_odd)
    = (~num . even + num . ~even) . ~new_odd
    = (num xor even) . ~new_odd
'''

def get_single_number(nums):
    odd, even = 0, 0
    for num in nums:
        odd = (num ^ odd) & ~even
        even = (num ^ even) & ~odd
    return odd | even

nums = [1,3,3,3]
assert get_single_number(nums) == 1

nums = [2,2,3,2]
assert get_single_number(nums) == 3

nums = [0,1,0,1,0,1,99]
assert get_single_number(nums) == 99
