def factorial(a):
    factorial_result = 1
    for i in range(a, 0, -1):
        factorial_result *= i
    return factorial_result


def factorial_division(a, b):
    a = factorial(a)
    b = factorial(b)
    division = a / b
    return division


num_1 = int(input())
num_2 = int(input())
result = factorial_division(num_1, num_2)
print(f"{result:.2f}")

