joltages = [0]  # initialize with socket 0
with open("input10.txt") as f:
    for line in f:
        joltages.append(int(line.strip()))

joltages = sorted(joltages)
joltages.append(joltages[-1] + 3)  # device

ones = threes = previous = 0
for i in joltages:
    if i - previous == 1:
        ones += 1
    elif i - previous == 3:
        threes += 1

    previous = i

print(ones * threes)

seen = {0: 1}
for idx, i in enumerate(joltages):
    if i not in seen:
        seen[i] = sum([seen[previous] for previous in joltages[max(0, idx - 3):idx] if 0 < i - previous <= 3])

print(seen[i])
