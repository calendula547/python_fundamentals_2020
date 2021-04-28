input_string = input()
counter = 1
for i in range(len(input_string)):
    if i+1 < len(input_string):
        if input_string[i] == input_string[i+1]:
            counter += 1
        else:
            print(input_string[i], end="")
            counter = 1
    else:
        print(input_string[i])
