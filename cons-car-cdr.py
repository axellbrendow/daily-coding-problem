def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair): # first
    return pair(lambda a, b: a)

def cdr(pair): # last
    return pair(lambda a, b: b)

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
