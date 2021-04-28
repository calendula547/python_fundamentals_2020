allowed_quantity = int(input())
days = int(input())
ornament_current = 0
tree_skirt_current = 0
tree_lights_current = 0
tree_garlands_current = 0

ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15
ornament_total = 0
tree_skirt_total= 0
tree_garlands_total = 0
tree_lights_total = 0
christmas_spirit = 0

for i in range(1, days+1):
    if i % 2 == 0:
        
        ornament_total += ornament_set_price * i
        christmas_spirit += 5
    if i % 3 == 0:
        tree_skirt_total += 2 * (tree_skirt_price * i)
        tree_garlands_total += 2 * (tree_garlands_price * i)
        christmas_spirit += 13
    if i % 5 == 0:
        tree_lights_total += tree_lights_price * i
        christmas_spirit += 17
    if i % 3 and i % 5:
        christmas_spirit += 30
    if i % 10 == 0:
        christmas_spirit -= 10
        tree_garlands_total += 1
        tree_skirt_total += 1
        tree_lights_total += 1
    if i % 11 == 0:
        allowed_quantity += 2

if days == 10:
        christmas_spirit -= 30

total_cost = ornament_total + tree_lights_total + tree_garlands_total + tree_skirt_total
print(f"Total cost: {total_cost} ")
print(f"Total spirit: {christmas_spirit}")
