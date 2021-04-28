single_string = input()
for symbol in range(len(single_string)):
    if single_string[symbol] == ":":
        print(single_string[symbol] + single_string[symbol + 1])