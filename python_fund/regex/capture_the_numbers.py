import re
sequence = input()
match = r"\d+"
while True:
    if not sequence:
        break
    matches = re.findall(match, sequence)
    for num in matches:
        print(num, end=" ")
    sequence = input()