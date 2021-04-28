version = list(input().split("."))


def greater_num(num_list):
    int_version = int("".join(num_list))
    next_version = int_version + 1
    result_version = [int(x) for x in str(next_version)]

    return result_version


next_version_result = (greater_num(version))
print('.'.join(str(el) for el in next_version_result))


