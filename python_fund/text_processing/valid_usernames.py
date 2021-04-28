def valid_usernames_lenght(name):
    if 3 <= len(name) <= 16:
        return True

def valid_usermanes_symbols(name):
    if name.isalnum() or  "_" in name or "-" in name:
        return True


username = input().split(", ")

for name in username:
    is_valid = False
    if valid_usernames_lenght(name) and valid_usermanes_symbols(name):
        is_valid = True
        print(name)


