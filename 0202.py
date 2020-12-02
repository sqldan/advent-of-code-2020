import re

good = 0
pol = re.compile("(?P<p1>\d+)-(?P<p2>\d+) (?P<c>\w): (?P<pw>.*)")
with open("input02.txt") as f:
    for line in f:
        m = pol.match(line)

        p1 = int(m.group('p1')) - 1
        p2 = int(m.group('p2')) - 1
        c = m.group('c')
        pw = m.group('pw')

        if (pw[p1] == c) ^ (pw[p2] == c):
            good += 1

print(good)
