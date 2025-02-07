def is_odd(num):
    return num % 2 == 1


def run_tests(tests):
    num_successes = 0
    num_failures = 0
    for test in tests:
        function = test['function']
        test_input = test['input']
        desired_output = test['output']
        if isinstance(test_input, tuple):
            actual_output = function(*test_input)
        else:
            actual_output = function(test_input)

        if actual_output == desired_output:
            num_successes += 1
        else:
            num_failures +=1
            function_name = function.__name__
            print('')
            print(f'{function_name} failed on input {test_input}')
            print(f'\t Actual output : {actual_output}')
            print(f'\t Desired output : {desired_output}')
    print(f'Testing complete for with {num_successes} Successes and {num_failures} Failures')


def create_tests(func_name, data):
    tests = []
    for input,output in data:
        tests.append({
            'function': func_name,
            'input': input,
            'output': output
        })
    return tests

def create_and_run_tests(func_name, data):
    run_tests(create_tests(func_name, data))


is_odd_data = [(2, False), (3, True)]

if __name__ == "__main__":
    create_and_run_tests(is_odd, is_odd_data)

