from test import create_tests, run_tests
import random

tests = []

def sim_probability(num_heads, num_flips):
    n = 10000
    count_exact = 0
    for _ in range(n):
        counter = 0
        for _ in range(num_flips):
            if random.random() < .5:
                counter += 1
        if counter == num_heads:
            count_exact += 1
    print(f'Looking for exactly {num_heads} flips in {num_flips} flips')
    print(f'After {n} trials, got {count_exact} attempt equal that')

num_flips = 10
for i in range(num_flips+1):
    sim_probability(i, num_flips)

run_tests(tests)