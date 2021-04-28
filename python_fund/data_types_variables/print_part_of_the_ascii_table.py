start_symbol = int(input())
stop_symbol = int(input())

for i in range(start_symbol, stop_symbol+1):
    print(f'{chr(i)} ', end="")
