number = int(input())

positives = []
negatives = []

for i in range(number):
    new_num = int(input())
    if new_num >= 0:
        positives.append(new_num)
    else:
        negatives.append(new_num)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")