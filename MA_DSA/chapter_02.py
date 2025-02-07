from test import create_tests, run_tests

tests = []
def any_to_decimal(string, base):
    res = 0
    dic = {
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15
    }
    for i in range(len(string)):        
        if string[i] in dic:
            digit = dic[string[i]]
        else:
            digit = int(string[i])
        exponent = len(string) - 1 - i
        res += digit * base ** exponent 
            
    return str(res)

any_to_decimal_data = [(("11010", 2), "26"), (("11111", 2), "31"), (('A', 16), '10'), (('AF4D',16), '44877')]
tests += create_tests(any_to_decimal, any_to_decimal_data)

def decimal_to_any(string, base):
    dic = {
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F'
    }
    num = int(string)
    res = ''
    max_total = 0
    exp = -1
    while max_total <= 0 or max_total < num:
        exp+= 1
        max_total = base ** exp

    exp -= 1
    
    while exp > -1:
        mult = base ** exp
        div = num // mult
        if div in dic:
            res += str(dic[div])
        else:
            res += str(div)
        num -= div * mult
        exp -= 1
    return res

decimal_to_any_data = [(('26', 2), '11010'), (('44877', 16), "AF4D")]
tests += create_tests(decimal_to_any, decimal_to_any_data)

def any_to_any(string, starting_base, ending_base):
    res = any_to_decimal(string, starting_base)
    return decimal_to_any(res, ending_base)

any_to_any_data = [(('26', 10, 16), '1A'), (('11010', 2, 10), '26')]
tests += create_tests(any_to_any, any_to_any_data)

run_tests(tests)