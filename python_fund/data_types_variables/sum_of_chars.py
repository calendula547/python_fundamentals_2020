num_of_lines = int(input())
sum_chars = 0
for i in range(0, num_of_lines):
    new_char = input()
    sum_chars += ord(new_char)
print(f'The sum equals: {sum_chars}')