def calculate(operator, num_one, num_two):
    if operator == "multiply":
        return num_one * num_two
    if operator == "divide":
        return int(num_one/num_two)
    if operator == "add":
        return num_one + num_two
    if operator == "subtract":
        return num_one - num_two


operation = input()
first_num = int(input())
second_num = int(input())

print(calculate(operation, first_num, second_num))
