num_snowballs = int(input())
snowball_high_value = 0
snowball_high_snow = 0
snowball_high_time = 0
snowball_high_quality = 0

for i in range(1, num_snowballs + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = int((snowball_snow/snowball_time) ** snowball_quality)
    if snowball_value > snowball_high_value:
        snowball_high_value = snowball_value
        snowball_high_snow = snowball_snow
        snowball_high_time = snowball_time
        snowball_high_quality = snowball_quality

print(f'{snowball_high_snow} : {snowball_high_time} = {snowball_high_value} ({snowball_high_quality})')
