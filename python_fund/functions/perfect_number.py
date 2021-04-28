def perfect_number(num):
    is_perfect = False
    sum_divisors = 0
    for i in range(1, num+1):
        if num % i == 0:
            sum_divisors += i
    if num == sum_divisors // 2:
        is_perfect = True
    return is_perfect


number = int(input())
result = perfect_number(number)
if result is True:
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
