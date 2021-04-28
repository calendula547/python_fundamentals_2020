nums = list(map(int, input().split(" ")))
invert_nums = []
for num in nums:
    if int(num) == 0:
        num = 0
    if int(num) > 0:
        num = - num
    else:
        num = abs(num)
    invert_nums.append(num)
print(invert_nums)
