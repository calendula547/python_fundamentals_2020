fires = list(input().split("#"))
water_at_begin = int(input())
fire_type = None
every_fire = [[i] for i in fires]

for i in range(len(every_fire)):
    #for j in range(len(every_fire[i])):
        #print(every_fire[i][j])
   #for j in range(len(every_fire[i])):
    if 1 <= int(every_fire[i][2]) <= 50:
        fire_type = "Low"
    elif 51 <= int(every_fire[i][2]) <= 80:
        fire_type = "Medium"
    elif 81 <= int(every_fire[i][2]) <= 125:
        fire_type = "High"
    print(fire_type)









