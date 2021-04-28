import re

text = input()

user_pattern = r"( |^)[a-z\d]+([\.\-_][a-z\d]+)*"
host_pattern = r"[a-z]+(\-[a-z]+)*(\.[a-z]+(\-[a-z]+)*){1,}"
pattern = rf"{user_pattern}@{host_pattern}"

matches = re.finditer(pattern, text)
for match in matches:
    mail = match[0].strip()
    print(mail)


