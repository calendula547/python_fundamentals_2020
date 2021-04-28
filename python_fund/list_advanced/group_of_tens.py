nums_list = list(map(int, input().split(", ")))


def find_boundary(numbers):
    boundary = None
    max_num = max(numbers)
    if max_num % 10 == 0:
        boundary = max_num
    else:
        boundary = (max_num - max_num % 10) + 10
    return boundary


boundary_final = find_boundary(nums_list)
current_boundary = 10
while nums_list is not []:
    current_group = list(filter((lambda x: x <= current_boundary), nums_list))
    print(f"Group of {current_boundary}'s: {current_group}")
    nums_list = [num for num in nums_list if num not in current_group]
    current_boundary += 10
    if current_boundary > boundary_final:
        break

