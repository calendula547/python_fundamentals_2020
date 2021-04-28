def characters_in_range(a, b):
    string_between_chars = ""
    for i in range(a+1, b):
        string_between_chars += chr(i) + " "
    return string_between_chars


first_char = ord(input())
second_char = ord(input())

print(characters_in_range(first_char, second_char))

