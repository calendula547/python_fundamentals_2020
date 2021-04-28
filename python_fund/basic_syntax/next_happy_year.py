str_year = (input())
year = int(str_year) + 1
str_year = str(year)

while True:
    if len(str_year) == len(set(str_year)):
        print(int(str_year))
        break
    else:
        year = int(str_year) + 1
        str_year = str(year)










