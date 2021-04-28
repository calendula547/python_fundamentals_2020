def is_palindrome(number):
    it_is_palindrome = False
    if len(number) == 1:
        it_is_palindrome = True
    for char in range(len(element)//2):
        if element[char] == element[len(element) - 1 - char]:
            it_is_palindrome = True
        else:
            it_is_palindrome = False
    return it_is_palindrome


list_numbers = list(input().split(", "))
for element in list_numbers:
    print(is_palindrome(element))
