number = int(input())
word = input()

common_string = [input() for _ in range(number)]
word_string = [element for element in common_string if word in element]

print(common_string)
print(word_string)


