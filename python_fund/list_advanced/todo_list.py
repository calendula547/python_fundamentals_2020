notes = []

while True:
    command = input()
    if command == "End":
        break
    tokens = command.split("-")
    importance = int(tokens[0])
    note = tokens[1]
    notes.append((importance, note))


def sort_fn(element):
    return element[0]


sorted_tasks = sorted(notes, key=sort_fn)
print([task[1] for task in sorted_tasks])