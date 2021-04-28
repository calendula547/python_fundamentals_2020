import re
input_text = input()
pattern = r">>([A-Z][A-Za-z]+)<<([\d]+(\.\d+)*)!(\d+)"
print("Bought furniture:")
price_list = []
quantity_list = []
while input_text != "Purchase":
    match = re.match(pattern, input_text)
    if match is not None:
        found_article = match.group(1)
        print(found_article)
        price_list.append(float(match.group(2)))
        quantity_list.append(int(match.group(4)))

    input_text = input()
print("Total money spend: ", end="")

result = [price_list[i] * quantity_list[i] for i in range(len(price_list))]
total_price = sum(result)
print(f"{total_price:.2f}")




