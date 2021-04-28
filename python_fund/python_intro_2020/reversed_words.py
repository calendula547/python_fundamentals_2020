string_word = input()
reversed_string = ""
len_string = len(string_word)

for i in range(len_string - 1, -1, -1):
    print(string_word[i], end="")

