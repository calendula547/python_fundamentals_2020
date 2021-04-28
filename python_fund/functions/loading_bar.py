def loading_bar(num):
    unit_num = num // 10
    list_bar = []
    for i in range(0, unit_num):
        list_bar += "%"
    for i in range(unit_num, 10):
        list_bar += "."
    return "".join(list_bar)


number = int(input())
if number < 100:
    print(f"{number}% ", end="")
    print("[", end="")
    print(loading_bar(number), end="")
    print("]")
    print("Still loading...")
else:
    print("100% Complete!")
    print("[", end="")
    print(loading_bar(number), end="")
    print("]")



