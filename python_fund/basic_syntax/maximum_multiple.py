divisor = int(input())
bound = int(input())
max_num = -93829345678524578457898

for num in range(bound, divisor-1, -1):
    if num % divisor == 0:
        if num > max_num:
            max_num = num

print(max_num)