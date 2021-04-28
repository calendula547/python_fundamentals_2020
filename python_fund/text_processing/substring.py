string_to_remove = input()
input_string = input()

while string_to_remove in input_string:
    input_string = input_string.replace(string_to_remove, " ")
    input_string = input_string.split(" ")
    input_string = "".join(input_string)
print(input_string)