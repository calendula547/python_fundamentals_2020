n = int(input())
capacity = 0

for i in range(0, n):
    new_liters = int(input())

    if capacity + new_liters > 255:
        print("Insufficient capacity!")
    else:
        capacity += new_liters

print(capacity)