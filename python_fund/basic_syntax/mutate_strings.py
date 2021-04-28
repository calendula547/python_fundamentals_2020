first_word = input()
second_word = input()
length = len(first_word)
first = first_word
second = ""
first_list = []
second_list = []


for j in first_word:
    first = first_word.replace(j, '', 1)
    first_word = first
    first_list.append(first_word)

for i in second_word:

    second_word = second + i
    second = second_word
    second_list.append(second)

result = [j + i for i, j in zip(first_list, second_list)]

unique_result = []

for i in result:
    if i not in unique_result:
        unique_result.append(i)

for i in unique_result:
    print(i)







