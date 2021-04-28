simple_text = input()
simple_text = "".join(simple_text)
ciphered_text = []
for symbol in simple_text:
    symbol = ord(symbol) + 3
    ciphered_text.append(chr(symbol))
print("".join(ciphered_text))





