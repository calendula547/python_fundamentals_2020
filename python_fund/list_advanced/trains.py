count_wagons = int(input())
train = [0 for num in range(count_wagons)]

input_command = input()
while input_command != "End":
    commands = input_command.split(" ")
    command = commands[0]

    if command == "add":
        last_index = len(train) - 1
        train[last_index] += int(commands[1])
    elif command == "insert":
        train[int(commands[1])] += int(commands[2])
    elif command == "leave":
        index = int(commands[1])
        train[index] -= int(commands[2])

    input_command = input()
print(train)

