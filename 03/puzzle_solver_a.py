import re

file = open("puzzle_input.txt", "r")

lines = file.readlines()

text = "\n".join(lines)

regex = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(regex, text)

values = (int(a) * int(b) for a, b in matches)

print(sum(values))
 