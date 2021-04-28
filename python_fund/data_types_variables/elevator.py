number_of_people = int(input())
capacity = int(input())
number_of_course = None

if number_of_people < capacity:
    number_of_course = 1
elif number_of_people % capacity == 0:
    number_of_course = int(number_of_people/capacity)
else:
    number_of_course = int(number_of_people/capacity) + 1

print(number_of_course)


