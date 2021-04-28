
def num_count(password):
    is_valid = False
    length = len(password)

    if 6 <= length <= 10:
        is_valid = True
        return is_valid
    else:
        return is_valid


def only_letters_and_digits(password):
    is_valid = False

    valid_letters = 0
    for element in password:
        if 48 <= ord(element) <= 57 or 65 <= ord(element) <= 90 or 97 <= ord(element) <= 122:
            valid_letters += 1
    if valid_letters == len(password):
        is_valid = True
        return is_valid
    else:
        return is_valid


def at_least_two_digits(password):
    is_valid = False
    nums_count = 0
    for element in password:
        if 48 <= ord(element) <= 57:
            nums_count += 1
    if nums_count >= 2:
        is_valid = True
        return is_valid
    else:
        return is_valid


def password_validator(password):

    result_1 = num_count(password)
    if result_1 is False:
        print("Password must be between 6 and 10 characters")
    result_2 = only_letters_and_digits(password)
    if result_2 is False:
        print("Password must consist only of letters and digits")
    result_3 = at_least_two_digits(password)
    if result_3 is False:
        print("Password must have at least 2 digits")
    if result_1 is True and result_2 is True and result_3 is True:
        print("Password is valid")


text = input()
password_validator(text)




