nums = list(map(int, (input().split(", "))))
even_nums_indices = []

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        even_nums_indices.append(i)
print(even_nums_indices)


