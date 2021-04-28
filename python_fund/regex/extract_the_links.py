import re
sequence = input()
sub_domain = r"(www.\b)"
domain = r"([A-Za-z\d\-]+)"
domain_extension = r"((\b.[a-z]+)+)"
pattern = rf"({sub_domain}{domain}{domain_extension})"
while True:
    if not sequence:
        break
    matches = re.search(pattern, sequence)
    if matches is not None:
        print(matches.group(1))
    sequence = input()