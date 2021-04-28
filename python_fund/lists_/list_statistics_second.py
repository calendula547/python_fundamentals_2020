number = int(input())

numbers = [int(input()) for _ in range(number)]
positives = [num for num in numbers if num >= 0]
negatives = [num for num in numbers if num < 0]

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")
