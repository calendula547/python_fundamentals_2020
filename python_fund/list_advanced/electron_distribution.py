electron_count = int(input())


def level_count_fn(number_of_electrons):
    level_num = 0
    electron_levels = []
    while number_of_electrons > 0:
        current_level_max_count = 2 * (level_num + 1) ** 2
        if current_level_max_count <= number_of_electrons:
            electron_levels.append(current_level_max_count)
        else:
            electron_levels.append(number_of_electrons)
        number_of_electrons -= current_level_max_count
        level_num += 1
    return electron_levels


print(level_count_fn(electron_count))