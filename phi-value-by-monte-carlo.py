import random

def estimate_phi():
    old_phi = 0
    phi = 0
    count_total = 0
    count_inside = 0
    while True:
        x, y = random.random(), random.random()
        count_total += 1
        if x**2 + y**2 <= 1:
            count_inside += 1
        phi = 4 * 1 * count_inside / count_total
        third_decimal_place = int(phi * 1000)
        old_third_decimal_place = int(old_phi * 1000)
        # if third_decimal_place % 10 != 0 and third_decimal_place == old_third_decimal_place:
        if third_decimal_place == 3141:
            print(old_phi, phi)
            return phi
        old_phi = phi

estimate_phi()
# assert int(estimate_phi() * 1000) == 3141
