nums_list = list(map(int, input().split(", ")))
beggars = int(input())
sums = 0
sums_for_beggar = []

for beggar in range(beggars):
    for num in range(0, len(nums_list), beggars):
        sums += nums_list[num]
    if len(nums_list) != 0:
        nums_list.pop(0)
        sums_for_beggar.append(sums)
        sums = 0
    else:
        break
if beggars > len(nums_list):
    sums_for_beggar += ([0] * (beggars - len(sums_for_beggar)))
print(sums_for_beggar)


