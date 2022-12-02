import string
from itertools import zip_longest

letters = string.ascii_letters

with open('input.txt', 'r') as f:
    lines = [l.strip('\n') for l in f.readlines()]

total = 0
groups = list(zip_longest(*[iter(lines)]*3, fillvalue=''))

for (a, b, c) in groups:
    total += letters.index([x for x in a if x in b and x in c][0]) + 1

print(total)