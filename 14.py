import re
import math
re_mem = re.compile("^mem\[(\d+)\] = (\d+)$")
mem = {}
with open("2020/input14.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith("mask"):
            mask = line[7:]
        else:
            m = re_mem.match(line)
            addr, val = m.groups()
            value = f"{int(val):036b}"
            result = "".join([v if m == 'X' else m for v, m in zip(value, mask)])
            mem[int(addr)] = result

print(sum(int(v, 2) for v in mem.values()))

mem = {}
with open("2020/input14.txt") as f:
    for line in f:
        line = line.strip()
        if line.startswith("mask"):
            mask = line[7:]
        else:
            m = re_mem.match(line)
            addr, val = m.groups()
            value = f"{int(addr):036b}"
            result = []
            for v, m in zip(value, mask):
                if m == "0":
                    result.append(v)
                else:
                    result.append(m)
            result = "".join(result)
            xs = result.count("X")
            for i in range(int(math.pow(2, xs))):
                tmp = result
                for s in f"{i:0{xs}b}":
                    tmp = tmp.replace("X", s, 1)
                mem[(int(tmp, 2))] = int(val)

print(sum(mem.values()))
