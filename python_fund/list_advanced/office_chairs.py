rooms_num = int(input())
free_chairs = 0
enough_chairs = 0
for i in range(rooms_num):
    chairs = input().split(" ")
    total_chairs = [el for el in chairs[0]]
    if len(total_chairs) >= int(chairs[1]):
        free_chairs += len(total_chairs) - int(chairs[1])
        enough_chairs += 1
    else:
        diff = int(int(chairs[1]) - len(total_chairs))
        print(f"{diff} more chairs needed in room {i + 1}")
if rooms_num == enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")

