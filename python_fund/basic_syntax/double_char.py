text = input()
double_text = ""
length = len(text)
for i in range(0, length):
    letter = text[i]
    double_text += letter + letter
print(double_text)