from test import create_tests, run_tests

tests = []

def five_by_three_sub_4(num):
    if num == 1:
        return 5
    prev_term = five_by_three_sub_4(num - 1)
    return prev_term * 3 - 4

five_by_three_sub_4_data = [(2, 11), (3, 29)]
tests += create_tests(five_by_three_sub_4, five_by_three_sub_4_data)

def collatz(num):
    if num == 1:
        return 25
    prev_term = collatz(num -1)
    return prev_term / 2 if prev_term % 2 == 0 else prev_term * 3 + 1

collatz_data = [(2, 76), (3, 38), (4, 19)]
tests += create_tests(collatz, collatz_data)

def fib(num):
    if num == 1:
        return 0
    if num == 2:
        return 1
    return fib(num -1) + fib (num - 2)

fib_data = [(3, 1), (4, 2), (5, 3), (6, 5)]
tests += create_tests(fib, fib_data)

def prod(num):
    if num == 1:
        return 2
    if num == 2:
        return -3
    return prod(num -1) * prod(num -2)

prod_tests = [(3, -6), (4, 18), (5, -6*18)]
tests += create_tests(prod, prod_tests)

run_tests(tests)