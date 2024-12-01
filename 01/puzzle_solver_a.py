file = open("puzzle_input.txt", 'r')

list_rows = file.readlines()

list_a, list_b = zip(*(item.split() for item in list_rows))

list_a = sorted(list_a)
list_b = sorted(list_b)

pairs = list(zip(list_a, list_b))

print(pairs[:5])

diffs = (abs(int(left) - int(right)) for left, right in pairs)

print(sum(diffs))