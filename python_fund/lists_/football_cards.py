card_string = list(input().split(" "))
card_set = set(card_string)
count_a = 0
count_b = 0
for element in card_set:
    if "A" in element:
        count_a += 1
    elif "B" in element:
        count_b += 1
    else:
        break

print(f"Team A - {11 - count_a}; Team B - {11 - count_b}")
if count_a > 4 or count_b > 4:
    print("Game was terminated")
