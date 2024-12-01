from collections import Counter
from functools import reduce

file = open("puzzle_input.txt", 'r')

lines = file.readlines()

column_a, column_b = zip(*(map(int, item.split()) for item in lines))

counts_b = Counter(column_b)

print(type(counts_b))
print(counts_b.most_common(3))

result = reduce(lambda acc, x: acc + (x * counts_b[x]), column_a, 0)

print(result)