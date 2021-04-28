def smallest_number(a, b, c):
    smallest_num = None
    if c > a < b:
        smallest_num = a
    if a > c < b:
        smallest_num = c
    if a > b < c:
        smallest_num = b
    return smallest_num


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(smallest_number(first_num, second_num, third_num))