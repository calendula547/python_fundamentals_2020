key_value = int(input())
num_of_lines = int(input())
decrypted_word = ''

for i in range(num_of_lines):
    letter = input()
    letter = ord(letter) + key_value
    modified_letter = chr(letter)
    decrypted_word += modified_letter
print(decrypted_word)