number = int(input())

for i in range(number):
    for j in range(number):
        for k in range(number):
            char_one = chr(97 + i)
            char_two = chr(97 + j)
            char_three = chr(97 + k)

            print(f"{char_one}{char_two}{char_three}")
