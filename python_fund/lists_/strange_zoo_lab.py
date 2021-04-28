string_one = input()
string_two = input()
string_three = input()

# first solution

#final_string = [string_one, string_two, string_three]
#final_string.reverse()
#print(final_string)

 #second solution

final_string = [string_one, string_two, string_three]
final_string[0], final_string[2] = final_string[2], final_string[0]
print(final_string)

# third solution




