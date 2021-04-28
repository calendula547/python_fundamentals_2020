employee_happiness = [int(happiness) for happiness in input().split(" ")]
happiness_factor = int(input())

greater_employee_happiness = list(map(lambda h: h*happiness_factor, employee_happiness))
average_happiness = sum(greater_employee_happiness) / len(greater_employee_happiness)


