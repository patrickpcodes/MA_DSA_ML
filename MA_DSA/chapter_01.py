from test import create_tests, run_tests

tests = []

def check_if_symmetric(data):
    for i in range(len(data)):
        if i > len(data) - i:
            return True
        if data[i] != data[len(data)-i-1]:
            return False
    return True

sym_data = [("racecar", True), ("Patrick", False), ("a", True)]
tests += create_tests(check_if_symmetric, sym_data)

def convert_to_numbers(data):
    res = []
    for d in data:
        if d == " ":
            res.append(0)
        else:
            res.append(ord(d) - ord('a') + 1)
    return res

con_num_data = [("a cat", [1, 0 ,3,1,20]), ("abcdz", [1, 2, 3, 4, 26])]
tests += create_tests(convert_to_numbers, con_num_data)

def convert_to_letters(data):
    res = ""
    num_to_str_dict = {
        0: ' ',
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'i',
        10: 'j',
        11: 'k',
        12: 'l',
        13: 'm',
        14: 'n',
        15: 'o',
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z'
    }
    for d in data:
        res += num_to_str_dict[d]
    return res

con_lett_data = [( [1, 0 ,3,1,20],"a cat",), ([1, 2, 3, 4, 26], "abcdz")]
tests += create_tests(convert_to_letters, con_lett_data)

def get_intersection(array1, array2):
    res = []
    for a in array1:
        if a in array2:
            res.append(a)
    return res

intersect_data = [(([1, 2], [1, 3]), [1]), (([2, 3, 4], [1]), []), (([2, 3, 4, 5],[1, 2, 3]), [2, 3])]
tests += create_tests(get_intersection, intersect_data) 

def get_union(array1, array2):
    res = []
    for a in array1:
        res.append(a)
    for b in array2:
        if b not in res:
            res.append(b)
    return res
union_data = [(([1, 2, 3], [1, 4]), [1, 2, 3, 4]), (([1, 2], [2]), [1, 2]), (([1], [1]), [1])]
tests += create_tests(get_union, union_data)

def count_characters(string):
    dic = {}
    for s in string:
        if s in dic:
            dic[s] = dic[s] + 1
        else:
            dic[s] = 1
    return dic

count_char_data = [("cat", {'a':1, 'c':1, 't':1}), ('bob oh bob', {'b':4, ' ':2, 'o': 3, 'h':1})]
tests += create_tests(count_characters, count_char_data)

def is_prime(num):
    mid = num //2 + 1
    for i in range(2, mid):
        if num % i == 0:
            return False
    return True
prime_data = [(4, False), (13, True), (121, False), (773, True)]
tests += create_tests(is_prime, prime_data)
run_tests(tests)