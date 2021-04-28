input_num = int(input())
is_prime = False

if input_num == 0:
    is_prime = False
else:
    for i in range(2, 10):
        if input_num % i == 0:
            is_prime = False
            break
        else:
            is_prime = True

print(is_prime)



