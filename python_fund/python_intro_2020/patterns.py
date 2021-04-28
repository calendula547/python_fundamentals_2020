number = int(input())

for i in range(1, number + 1, 1):
    for j in range(0, i):
        print("*", end="")
        j += 1
    print()
for i in range(number, 1, -1):
    for j in range(0, i-1):
        print("*", end="")
        j += 1
    print()
