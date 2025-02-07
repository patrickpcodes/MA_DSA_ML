import random 
def random_draw(distribution):
    cummulative_distribution = []
    cummulative_sum = 0
    for i in distribution:
        cummulative_sum += i
        cummulative_distribution.append(cummulative_sum)
    r = random.random()
    for i,value in enumerate(cummulative_distribution):
        if r <= value:
            return i

def test_random_draw():
    distributions = [
        [0.5, 0.5],
        [0.4, 0.2, 0.2, 0.2],
        [0.1, 0.1, 0.1, 0.7],
        [0.25, 0.25, 0.25, 0.25]
    ]
    num_samples = 100000

    for distribution in distributions:
        counts = [0] * len(distribution)
        
        for _ in range(num_samples):
            index = random_draw(distribution)
            counts[index] += 1

        proportions = [count / num_samples for count in counts]
        print(f"Distribution: {distribution}")
        print(f"Proportions: {proportions}")
        print()

test_random_draw()
