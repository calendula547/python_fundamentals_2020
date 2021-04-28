text = input().split(" ")
text_lenght = len(text)
for i in range(text_lenght):
    print(text[i] * len(text[i]), end="")


