num_lines = int(input())
closing_brackets = 0
opening_brackets = 0

for i in range(num_lines):
    new_str = input()
    if new_str == ")":
        closing_brackets += 1
    if new_str == "(":
        opening_brackets += 1
if closing_brackets == opening_brackets:
    print("BALANCED")
else:
    print("UNBALANCED")
