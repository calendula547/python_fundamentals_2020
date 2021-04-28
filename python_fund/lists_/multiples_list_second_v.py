factor = int(input())
count = int(input())

multiple_list = [factor * i for i in range(1, count+1)]
print(multiple_list)