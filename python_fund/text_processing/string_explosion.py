input_string = input()
power = 0
i = 0
while i < len(input_string):
    ch = input_string[i]
    if ch == ">":
        power += int(input_string[i+1])
    elif power > 0:
        input_string = input_string[:i] + input_string[i+1:]
        i -= 1
        power -= 1
    i += 1

print(input_string)