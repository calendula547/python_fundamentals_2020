def get_a_num(sequence):
    digit = ""
    for el in sequence:
        if el.isdigit():
            digit += el
    return int(digit)


def char_position(letter):
    return ord(letter) - 96


def every_first_string(input_string):
    total_result = 0
    digit = get_a_num(input_string)
    if input_string[0].islower():
        first_letter = char_position(input_string[0].lower())
        result = digit * first_letter
    else:
        first_letter = char_position(input_string[0].lower())
        result = digit / first_letter
    total_result += result

    if input_string[-1].islower():
        last_letter = char_position(input_string[-1].lower())
        total_result = total_result + last_letter
    else:
        last_letter = char_position(input_string[-1].lower())
        total_result = total_result - last_letter

    return total_result


result_list = []
input_sequence = input().split()

for i in range(len(input_sequence)):
    result_list.append(every_first_string(input_sequence[i]))

sum_of_sum_and_subtract = 0.0
for i in range(len(result_list)):
    sum_of_sum_and_subtract += result_list[i]


print(f"{sum_of_sum_and_subtract:.2f}")

