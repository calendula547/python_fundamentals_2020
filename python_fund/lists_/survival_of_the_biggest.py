list_ints = list(map(int, input().split(" ")))
number = int(input())
removed_items = []
sorted_list = sorted(list_ints)
for i in range(number):
    removed_items.append(sorted_list.pop(0))

biggest_nums = [num for num in list_ints if num not in removed_items]
print(biggest_nums)