firstElf_List = []
secondElf_List = []

pairs, intersection = 0, 0

firstElf_ranges = []
secondElf_range = []

def get_range(r):
    n = tuple(int(c) for c in r.split("-"))

    return range(n[0], n[1] + 1)

def subset(x, y):
    return not(False in [z in y for z in x])

with open('input.txt', 'r') as f:
    for line in f:
        ar, br = line.split(",")

        a, b = get_range(ar), get_range(br)

        if subset(a, b) or subset(b, a): 
            pairs += 1

        if any(i in a for i in b):
            intersection += 1

    print(pairs)
    print(intersection)

        