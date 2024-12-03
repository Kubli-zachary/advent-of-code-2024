import itertools

def comp_asc(a, b) -> bool:
    if (a >= b):
        return False
    if (b - a > 3):
        return False
    return True

def comp_desc(a, b) -> bool:
    if (a <= b):
        return False
    if (a - b > 3):
        return False
    return True

# returns true if safe
def safety_check(row) -> bool:
    if (all(comp_asc(a, b) for a, b in itertools.pairwise(row))):
        return True
    if (all(comp_desc(a, b) for a, b in itertools.pairwise(row))):
        return True
    return False

file = open("puzzle_input.txt", "r")

data = file.readlines()
data = [x.split() for x in data]
data = [[int(x) for x in row] for row in data]

safety_checks = [safety_check(row) for row in data]
print(sum(safety_checks))
