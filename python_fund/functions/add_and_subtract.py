def sum_numbers(a, b):
    sum_nums = a + b
    return sum_nums


def subtract(a, b):
    subtraction = a - b
    return subtraction


def add_and_subtract(num_one, num_two, num_three):
    sum_nums = sum_numbers(num_one, num_two)
    result = subtract(sum_nums, num_three)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))
