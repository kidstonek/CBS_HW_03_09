from math import sqrt


def simple_check(num: int) -> bool:
    simple = True
    i = 2
    while i <= sqrt(num):
        if num % i == 0:
            simple = False
            break
        i += 1
    return simple


def simple_gen(qty: int) -> list:
    simple_numbers = []
    tmp_num = 2
    while True:
        if simple_check(tmp_num):
            simple_numbers.append(tmp_num)
        tmp_num += 1
        if qty == len(simple_numbers):
            break

    return simple_numbers
