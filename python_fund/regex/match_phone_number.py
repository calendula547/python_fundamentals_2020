import re

telephone_number_string = input()
pattern = r"(\+359([-|  ])2\2\d{3}\2\d{4}\b)"
result = re.findall(pattern, telephone_number_string)
print(", ".join([phone for phone, sep in result]))

