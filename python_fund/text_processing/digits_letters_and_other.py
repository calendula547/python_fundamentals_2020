input_string = input()
digit_list = []
letter_list = []
others = []

for symbol in input_string:
    if symbol.isdigit():
        digit_list.append(symbol)
    elif 90 >= ord(symbol) >= 65 or 122 >= ord(symbol) >= 97:
        letter_list.append(symbol)
    else:
        others.append(symbol)

print("".join(digit_list))
print("".join(letter_list))
print("".join(others))