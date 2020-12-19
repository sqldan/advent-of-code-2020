import re
# 2 = a, 118 = b
from pprint import pprint
from itertools import chain

lines = []
codes = {}
found = {}
with open("test.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        key, val = line.split(": ")
        key = int(key)
        if val == '"a"':
            found[key] = ['a']
        elif val == '"b"':
            found[key] = ['b']
        else:
            vals = val.split(" | ")
            nrs = [val.split() for val in vals]
            if len(nrs) == 1:
                nrs = [int(nr) for nr in nrs[0]]
                codes[key] = [nrs]

            else:
                nr0 = nrs[0]
                nr1 = nrs[1]
                nr0 = [int(nr) for nr in nr0]
                nr1 = [int(nr) for nr in nr1]
                codes[key] = [nr0, nr1]

pprint(codes)
pprint(found)

found_keys = set(found.keys())

for key, val in codes.items():
    if set(chain(*val)).issubset(found_keys):
        print(key)

# {2: ['aa', 'bb']