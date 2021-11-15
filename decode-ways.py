'''
Error: empty string

LEMBRAR DE COLOCAR NONLOCAL NAS VARIÁVEIS DO PYTHON DENTRO DE CLOSURES

variable_name = 0

def fun():
    nonlocal variable_name
    variable_name += 1
'''

def decode_ways(encoded):
    if len(encoded) == 0: return 0

    cache = {}

    def decode_ways_rec(i):
        if i in cache: return cache[i]
        if i == len(encoded):
            cache[i] = 1
            return 1
        if i > len(encoded):
            cache[i] = 0
            return 0

        ways = decode_ways_rec(i + 1)

        if (
            i + 1 < len(encoded) and (
                encoded[i] == '1' and '0' <= encoded[i + 1] <= '9' or
                encoded[i] == '2' and '0' <= encoded[i + 1] <= '6'
            )
        ):
            ways += decode_ways_rec(i + 2)

        cache[i] = ways
        return ways

    return decode_ways_rec(0)

assert decode_ways('') == 0
assert decode_ways('1') == 1
assert decode_ways('11') == 2
assert decode_ways('111') == 3
assert decode_ways('1111') == 5
assert decode_ways('11161') == 5
assert decode_ways('12161') == 5
assert decode_ways('13161') == 4
