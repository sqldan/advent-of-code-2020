with open("input13.txt") as f:
    ts = f.readline()
    ts = int(ts)
    input = f.readline()

lines = input.split(",")

nrs = []
for idx, line in enumerate(lines):
    if line != 'x':
        line = int(line)
        wait = line - idx % line
        nrs.append((line, wait % line))

first = 0
for bus, _ in nrs:
    wait = bus - ts % bus
    if not first or wait < first:
        answer1 = bus * wait
        first = wait

print(answer1)

start, _ = nrs.pop(0)
step = start
while nrs:
    start += step
    for bus, idx in nrs:
        if start % bus == idx:
            step *= bus
            nrs.remove((bus, idx))

print(start)