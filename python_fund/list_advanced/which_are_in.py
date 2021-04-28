first_list = list(input().split(", "))
second_list = list(input().split(", "))
result_list = []
for el in first_list:
    for item in second_list:
        if el in item:
            result_list.append(el)
            break
print(result_list)
