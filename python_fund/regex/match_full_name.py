import re
names_string = input()
regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
matches = re.findall(regex, names_string)
print(" ".join(matches))