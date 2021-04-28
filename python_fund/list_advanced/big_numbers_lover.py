num_list = list(input().split(" "))

num_list.sort()
num_list.sort(reverse=True)
reversed_list = "".join(num_list)
print(reversed_list)

