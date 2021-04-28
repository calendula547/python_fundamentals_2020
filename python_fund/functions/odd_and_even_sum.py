def odd_and_even_sum(a):
    odd_sum = 0
    even_sum = 0
    for element in a:
        num = int(element)
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
result = odd_and_even_sum(number)
print(result)

