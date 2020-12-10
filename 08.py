lines = []
with open("input08.txt") as f:
    for line in f:
        line = line.strip()
        op, val = line.split()
        lines.append((op, int(val)))


def get_acc(lines):
    l = len(lines)
    acc = 0
    seen = []
    i = 0
    while i not in seen:
        seen.append(i)
        op, val = lines[i]
        if op == "nop":
            i += 1
        elif op == "acc":
            acc += val
            i += 1
        elif op == "jmp":
            i += val

        if i >= l:
            return False, acc

    return True, acc

_, acc = get_acc(lines)
# answer 1
print(acc)
# answer 2
for idx, (chg, val) in enumerate(lines):
    newlines = lines[:]
    if chg == "jmp":
        newlines[idx] = ("nop", val)
    elif chg == "nop":
        newlines[idx] = ("jmp", val)
    else:
        continue

    seen, acc = get_acc(newlines)
    if not seen:
        print(acc)
        break
