original_string = list(map(str, input().split(" ")))
shuffles_num = int(input())

length = int(len(original_string)/2)
first_string = []
second_string = []
result_string = []
str_build = ""
for i in range(shuffles_num):
    for j in range(length):
        first_string += (original_string[j])
        second_string += (original_string[j + length])
        result_string += first_string + second_string

        #result_string = ' '.join(result_string)
    #for j in range(length):
        #first_string += original_string[j]
        #second_string += original_string[j+length]
        #result_string += first_string[j]
        #result_string += second_string[j]
    if i < length:
        original_string = result_string
        first_string = []
        second_string = []
        result_string = []
    else:
        print(result_string)
