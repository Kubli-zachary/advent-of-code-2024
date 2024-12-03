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
    ## ASCENDING

    upcheck = [not comp_asc(a, b) for a, b in itertools.pairwise(row)]
    # Counting errors ^ hence the not
    match sum(upcheck):
        case 0:
            return True  # Already non-decreasing
        case _: # Potentially optimizable by error count, but not worth the effort/ambiguity
            error_index = upcheck.index(True)
            # Try removing the element at error_index
            temp_row = row[:error_index] + row[error_index+1:]
            if all(comp_asc(a, b) for a, b in itertools.pairwise(temp_row)):
                return True
            # Try removing the element at error_index + 1
            temp_row = row[:error_index+1] + row[error_index+2:]
            if all(comp_asc(a, b) for a, b in itertools.pairwise(temp_row)):
                return True
            # Try removing the element at error_index - 1
            temp_row = row[:error_index-1] + row[error_index:]
            if all(comp_asc(a, b) for a, b in itertools.pairwise(temp_row)):
                return True

    ## DESCENDING

    downcheck = [not comp_desc(a, b) for a, b in itertools.pairwise(row)]
    # Counting errors ^ hence the not
    match sum(downcheck):
        case 0:
            return True  # Already non-increasing
        case _:
            error_index = downcheck.index(True)
            # Try removing the element at error_index
            temp_row = row[:error_index] + row[error_index+1:]
            if all(comp_desc(a, b) for a, b in itertools.pairwise(temp_row)):
                return True
            # Try removing the element at error_index + 1
            temp_row = row[:error_index+1] + row[error_index+2:]
            if all(comp_desc(a, b) for a, b in itertools.pairwise(temp_row)):
                return True
            # Try removing the element at error_index - 1
            temp_row = row[:error_index-1] + row[error_index:]
            if all(comp_desc(a, b) for a, b in itertools.pairwise(temp_row)):
                return True

    return False


file = open("puzzle_input.txt", "r")

data = file.readlines()
data = [x.split() for x in data]
data = [[int(x) for x in row] for row in data]

safety_checks = [safety_check(row) for row in data]
print(sum(safety_checks))
