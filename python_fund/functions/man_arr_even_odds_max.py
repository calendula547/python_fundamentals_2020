def max_even_odd(command, arr):
    result = None
    even_nums = []
    odd_nums = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even_nums.append(arr[i])
        else:
            odd_nums.append(arr[i])

    if command == "odd":
        max_odd_num = odd_nums[0]
        max_index = odd_nums.index(max_odd_num)
        for i in range(1, len(odd_nums)):
            if odd_nums[i] >= max_odd_num:
                max_odd_num = odd_nums[i]
                max_index = i
        result = max_index

    if command == "even":
        max_even_num = even_nums[0]
        max_index = even_nums.index(max_even_num)
        for i in range(1, len(even_nums)):
            if even_nums[i] >= max_even_num:
                max_even_num = even_nums[i]
                max_index = i
        result = max_index
    return result


current_command = input()
array_nums = list(map(int, input().split(" ")))
print(max_even_odd(current_command, array_nums))

