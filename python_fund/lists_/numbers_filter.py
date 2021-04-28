num = int(input())

numbers = [int(input()) for _ in range(num)]
command = input()
if command == "even":
    even_nums = [num for num in numbers if num % 2 == 0]
    print(even_nums)
elif command == "odd":
    odd_nums = [num for num in numbers if num % 2 != 0]
    print(odd_nums)
elif command == "negative":
    negatives = [num for num in numbers if num < 0]
    print(negatives)
elif command == "positive":
    positives = [num for num in numbers if num >= 0]
    print(positives)

