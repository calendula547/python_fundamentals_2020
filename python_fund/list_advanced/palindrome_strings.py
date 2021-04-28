words = list(input().split(" "))
searched_palindrome = input()


def is_palindrome(word):
    it_is_palindrome = False
    if len(word) == 1:
        it_is_palindrome = True
    for char in range(len(word)//2):
        if word[char] == word[len(word) - 1 - char]:
            it_is_palindrome = True
        else:
            it_is_palindrome = False
    return it_is_palindrome


palindromes = []
[palindromes.append(element) for element in words if is_palindrome(element) is True]

counter = 0
for i in range(len(palindromes)):
    if palindromes[i] == searched_palindrome:
        counter += 1
print(palindromes)
print(f"Found palindrome {counter} times")
