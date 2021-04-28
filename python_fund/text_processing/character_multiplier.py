entire_text = input().split(" ")
word_one = entire_text[0]
word_two = entire_text[1]
lenght = min(len(word_one), (len(word_two)))

total_sum = 0
for i in range(lenght):
    multiplied_nums = int(ord(word_one[i]))* int(ord(word_two[i]))
    total_sum += multiplied_nums
if len(word_one) != len(word_two):
    if len(word_one) > len(word_two):
        for i in range (lenght, len(word_one)):
            total_sum += int(ord(word_one[i]))
    else:
        for i in range (lenght, len(word_two)):
            total_sum += int(ord(word_two[i]))
print(total_sum)