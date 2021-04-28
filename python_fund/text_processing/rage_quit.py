def get_a_num(character):
    if character.isdigit():
        return int(character)


input_string = input()
letter_string = ""
result_string = ""
for i in range(len(input_string)):
    if get_a_num(input_string[i]):
        if i+1 < len(input_string) and get_a_num(input_string[i+1]):
            num = int(input_string[i] + input_string[i+1])
            letter_string = letter_string * num
        else:
            letter_string = letter_string * int(input_string[i])
        result_string += letter_string
        letter_string = ""
    else:
        if input_string[i] == "0":
            letter_string = ""
        else:
            letter_string += input_string[i]

result_string_set = set(result_string.lower())
print(f"Unique symbols used: {len(result_string_set)}")
print(result_string.upper())

