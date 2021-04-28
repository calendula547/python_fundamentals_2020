gifts_list = list(input().split())
command = input().split(" ")
while True:
    if "No" in command and "Money" in command:
        break
    if "OutOfStock" in command:
        for i in range(len(gifts_list)):
            if gifts_list[i] == command[1]:
                gifts_list[i] = None
    if "Required" in command:
        for i in range(len(gifts_list)):
            if int(command[2]) < len(gifts_list) and int(command[2]) == i:
                gifts_list[i] = command[1]
    if "JustInCase" in command:
        gifts_list[-1] = command[1]
    command = input().split(" ")

for i in range(len(gifts_list)):
    if gifts_list[i] is not None:
        print(gifts_list[i], end=" ")
