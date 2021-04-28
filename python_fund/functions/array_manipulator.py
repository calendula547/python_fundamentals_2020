import sys


def read_list():
    array_nums = list(map(int, input().split(" ")))
    return array_nums


def list_exchange(arr, ind):
    if 0 > ind or ind >= len(arr):
        result = "Invalid index"
        return result
    else:
        arr_split_1 = []
        arr_split_2 = []
        for i in range(len(arr)):
            if i <= ind:
                arr_split_1.append(arr[i])
            else:
                arr_split_2.append(arr[i])
        for i in range(len(arr_split_1)):
            arr_split_2.append(arr_split_1[i])
        return arr_split_2


def max_odd_even(nums, word):
    max_num = -sys.maxsize
    max_index = -1
    if word == "even":
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] >= max_num:
                max_num = nums[i]
                max_index = i
    else:
        for i in range(len(nums)):
            if nums[i] % 2 != 0 and nums[i] >= max_num:
                max_num = nums[i]
                max_index = i
    return max_index


def min_odd_even(nums, word):
    min_num = sys.maxsize
    min_index = -1
    if word == "even":
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <= min_num:
                min_num = nums[i]
                min_index = i
    else:
        for i in range(len(nums)):
            if nums[i] % 2 != 0 and nums[i] <= min_num:
                min_num = nums[i]
                min_index = i
    return min_index


def first_count_even_odd(nums, count, word):
    chosen_elements = []
    if word == "even":
        for num in nums:
            if num % 2 == 0 and len(chosen_elements) < count:
                chosen_elements.append(num)
    else:
        for num in nums:
            if num % 2 != 0 and len(chosen_elements) < count:
                chosen_elements.append(num)
    return chosen_elements


def last_count_even_odd(nums, count, word):
    chosen_elements = []
    reversed_nums = list(reversed(nums))
    if word == "even":
        for num in reversed_nums:
            if num % 2 == 0 and len(chosen_elements) < count:
                chosen_elements.append(num)
    else:
        for num in reversed_nums:
            if num % 2 != 0 and len(chosen_elements) < count:
                chosen_elements.append(num)
    reversed_chosen_elements = list(reversed(chosen_elements))
    return reversed_chosen_elements


def solve_the_problem():
    nums_list = read_list()
    current_command = input()

    while current_command != "end":
        arguments = current_command.split(" ")
        command = arguments[0]

        if command == "exchange":
            num_index = int(arguments[1])
            nums_exchanged = list_exchange(nums_list, num_index)
            if nums_exchanged == "Invalid index":
                print("Invalid index")
                current_command = input()
                continue
            else:
                nums_list = nums_exchanged

        if command == "max":
            type_odd_or_even = arguments[1]
            max_num_index = max_odd_even(nums_list, type_odd_or_even)
            if max_num_index != -1:
                print(max_num_index)
            else:
                print("No matches")

        if command == "min":
            type_odd_or_even = arguments[1]
            min_num_index = min_odd_even(nums_list, type_odd_or_even)
            if min_num_index != -1:
                print(min_num_index)
            else:
                print("No matches")

        if command == "first":
            num_count = int(arguments[1])
            type_odd_or_even = arguments[2]

            if num_count > len(nums_list):
                print("Invalid count")
                current_command = input()
                continue
            else:
                print(first_count_even_odd(nums_list, num_count, type_odd_or_even))

        if command == "last":
            num_count = int(arguments[1])
            type_odd_or_even = arguments[2]

            if num_count > len(nums_list):
                print("Invalid count")
                current_command = input()
                continue
            else:
                print(last_count_even_odd(nums_list, num_count, type_odd_or_even))

        current_command = input()

    print(nums_list)


solve_the_problem()



