def min_even_odd(command, arr):
    result = None
    even_nums = []
    odd_nums = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_nums.append(arr[i])
        else:
            odd_nums.append(arr[i])

    if command == "odd":
        if odd_nums == []:
            result = "No matches"
        else:
            min_odd_num = odd_nums[0]
            min_index = odd_nums.index(min_odd_num)
            for i in range(1, len(odd_nums)):
                if odd_nums[i] <= min_odd_num:
                    min_odd_num = odd_nums[i]
                    min_index = i
            result = min_index

    if command == "even":
        if even_nums == []:
            result = "No matches"
        else:
            min_even_num = even_nums[0]
            min_index = even_nums.index(min_even_num)
            for i in range(1, len(even_nums)):
                if even_nums[i] <= min_even_num:
                    min_even_num = even_nums[i]
                    min_index = i
            result = min_index
    return result


current_command = input()
array_nums = list(map(int, input().split(" ")))
print(min_even_odd(current_command, array_nums))