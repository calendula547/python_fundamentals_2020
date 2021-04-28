import re

pattern = r"\b_([a-zA-Z\d]+\b)"
text_string = input()

match = re.findall(pattern, text_string)
print(",".join(match))
