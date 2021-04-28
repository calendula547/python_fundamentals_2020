factor = int(input())
count = int(input())

multiple_list = []

for i in range(1, count+1):
    multiple_list.append(i * factor)
print(multiple_list)