H0_pos, M1_pos, M0_pos = 1, 3, 4

def smallest_that_is_greater_than(value_pos, max_value, datetime):
    smallest = chr(ord('9') + 1)
    for i in range(5):
        if i == value_pos or i == 2: continue
        if (
            datetime[i] <= max_value
            and datetime[i] > datetime[value_pos]
            and datetime[i] < smallest
        ):
            smallest = datetime[i]
    return smallest

def get_smallest_digit(datetime):
    smallest = chr(ord('9') + 1)
    for i in range(5):
        if i == 2: continue
        if datetime[i] < smallest:
            smallest = datetime[i]
    return smallest

def try_to_change_only_M1_or_M0(datetime):
    smallest_greater_than_M1 = smallest_that_is_greater_than(M1_pos, '5', datetime)
    if '0' <= smallest_greater_than_M1 <= '9':
        return smallest_greater_than_M1, get_smallest_digit(datetime)
    return chr(ord('0') - 1), chr(ord('0') - 1)

def try_to_change_only_H0_or_M1_or_M0(datetime):
    if datetime[0] == '2':
        smallest_greater_than_H0 = smallest_that_is_greater_than(H0_pos, '3', datetime)
    else:
        smallest_greater_than_H0 = smallest_that_is_greater_than(H0_pos, '9', datetime)
    if '0' <= smallest_greater_than_H0 <= '9':
        smallest_digit = get_smallest_digit(datetime)
        return smallest_greater_than_H0, smallest_digit, smallest_digit
    return chr(ord('0') - 1), chr(ord('0') - 1), chr(ord('0') - 1)

# H1 H0 : M1 M0
def next_closest_time(datetime):
    M0 = smallest_that_is_greater_than(M0_pos, '9', datetime)
    if '0' <= M0 <= '9':
        return datetime[0:4] + M0

    M1, M0 = try_to_change_only_M1_or_M0(datetime)
    if '0' <= M1 <= '9' and '0' <= M0 <= '9':
        return datetime[0:2] + ':' + M1 + M0

    H0, M1, M0 = try_to_change_only_H0_or_M1_or_M0(datetime)
    if '0' <= H0 <= '9' and '0' <= M1 <= '9' and '0' <= M0 <= '9':
        return datetime[0] + H0 + ':' + M1 + M0

    smallest_digit = get_smallest_digit(datetime)
    return (smallest_digit * 2) + ':' + (smallest_digit * 2)

assert next_closest_time('01:34') == '01:40'
assert next_closest_time('05:34') == '05:35'
assert next_closest_time('05:43') == '05:44'
assert next_closest_time('05:46') == '05:50'
assert next_closest_time('01:59') == '05:00'
assert next_closest_time('12:59') == '15:11'
assert next_closest_time('21:59') == '22:11'
assert next_closest_time('21:29') == '22:11'
assert next_closest_time('23:11') == '23:12'
assert next_closest_time('23:59') == '22:22'
