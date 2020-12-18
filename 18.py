import re
from math import prod

lines = []
with open("input18.txt") as f:
    for line in f:
        line = line.strip()
        lines.append(line)

re_bracket = re.compile("\([ +*0123456789]+\)")
re_math = re.compile("(\d+) ([+*]) (\d+)")
re_plus = re.compile("(\d+) \+ (\d+)")
re_times = re.compile("(\d+) \* (\d+)")

def solve(s, plus_first):
    if m := re_bracket.search(s):
        start, end = m.span()
        tot = solve(s[start + 1 : end - 1], plus_first)
        return solve(s[:start] + tot + s[end:], plus_first)

    elif not plus_first and re_math.search(s):
        m = re_math.search(s)
        start, end = m.span()
        l, op, r = m.groups()
        if op == "+":
            tot = int(l) + int(r)
        else:
            tot = int(l) * int(r)
        return solve(s[:start] + str(tot) + s[end:], plus_first)

    elif m := re_plus.search(s):
        start, end = m.span()
        tot = sum(int(g) for g in m.groups())
        return solve(s[:start] + str(tot) + s[end:], plus_first)

    elif m := re_times.search(s):
        start, end = m.span()
        tot = prod(int(g) for g in m.groups())
        return solve(s[:start] + str(tot) + s[end:], plus_first)

    
    return s

print(sum(int(solve(line, plus_first=False)) for line in lines))
print(sum(int(solve(line, plus_first=True)) for line in lines))
