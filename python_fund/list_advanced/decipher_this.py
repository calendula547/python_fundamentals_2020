secret_message = list(input().split(" "))
for word in secret_message:
    decipher_list = []
    list_word = [el for el in word]
    int_list = [n for n in list_word if n.isdigit()]
    result_int = int("".join(int_list))
    int_to_char = chr(result_int)
    letters = list(filter((lambda let: let not in int_list), list_word))
    letters[0], letters[-1] = letters[-1], letters[0]

    decipher_list.append(int_to_char)
    decipher_list.append(letters)
    flatList = [item for elem in decipher_list for item in elem]
    just_text = "".join(str(x) for x in flatList)
    print(just_text, end=" ")


