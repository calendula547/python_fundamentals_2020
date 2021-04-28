def revers_string(s):
   return ("".join(reversed(s)))

word = input()
while word != "end":
    reversed_string = revers_string(word)
    print(f"{word} = {reversed_string}")
    word = input()