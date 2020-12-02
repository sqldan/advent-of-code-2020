import re

good = 0
pol = re.compile("(?P<low>\d+)-(?P<high>\d+) (?P<c>\w): (?P<pw>.*)")
with open("input02.txt") as f:
    for line in f:
        m = pol.match(line)
        low = int(m.group('low'))
        high = int(m.group('high'))
        c = m.group('c')
        pw = m.group('pw')

        if low <= pw.count(c) <= high:
            good += 1

print(good)
