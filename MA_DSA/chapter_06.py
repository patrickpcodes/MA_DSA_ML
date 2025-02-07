from test import create_tests, run_tests

def create_array(arr):
    arr_copy = []
    for i in arr:
        arr_copy.append(i)
    return arr_copy

tests = []
def calc_cartesian_product(lsts):
    points = [[]]
    for lst in lsts:
        points_copy = create_array(points)
        extended_points = []
        for i in range(len(points_copy)):
            for val in lst:
                extended_point = create_array(points_copy[i])
                extended_point.append(val)
                extended_points.append(extended_point)
        points = extended_points
    

    return points
print(calc_cartesian_product([['a'], [1, 2, 3], ['Y', 'Z']]))
