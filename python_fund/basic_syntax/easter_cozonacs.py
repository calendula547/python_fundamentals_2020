budget = float(input())
flour_price = float(input())
egg_price = 75/100 * flour_price
milk_price = flour_price + (25/100 * flour_price)
need_milk_price = 0.250 * milk_price

colored_egg = 0
lose_egg = 0
total_colored_eggs = None
save_money = None

single_cozonac_price = flour_price + egg_price + need_milk_price
count_cozonacs = int(budget/single_cozonac_price)

for i in range(1, count_cozonacs + 1):
    colored_egg += 3
    if i % 3 == 0:
        lose_egg += i - 2

total_colored_eggs = colored_egg - lose_egg
save_money = f'{(budget - single_cozonac_price * count_cozonacs):.2f}'

print(f"You made {count_cozonacs} cozonacs! Now you have {total_colored_eggs} eggs and {save_money}BGN left.")



