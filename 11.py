from itertools import repeat
from pprint import pprint

lines = []
with open("input11.txt") as f:
    for line in f:
        lines.append(list(line.strip()))


WIDTH = len(lines[0])
HEIGHT = len(lines)
# pprint(lines)

changed = True
while changed:
    changed = False
    newlines = [row[:] for row in lines[:]]
    for row_idx, row in enumerate(newlines):
        for col_idx, col in enumerate(row):
            if col == ".": continue
            # above
            adj = 0
            if row_idx > 0:
                if col_idx > 0:
                    if newlines[row_idx - 1][col_idx - 1] == "#":
                        adj += 1
                if newlines[row_idx - 1][col_idx] == "#":
                    adj += 1
                if col_idx < WIDTH - 1:
                    if newlines[row_idx - 1][col_idx + 1] == "#":
                        adj += 1

            if col_idx > 0:
                if newlines[row_idx][col_idx - 1] == "#":
                    adj += 1
            if col_idx < WIDTH - 1:
                if newlines[row_idx][col_idx + 1] == "#":
                    adj += 1

            if row_idx < HEIGHT - 1:
                if col_idx > 0:
                    if newlines[row_idx + 1][col_idx - 1] == "#":
                        adj += 1
                if newlines[row_idx + 1][col_idx] == "#":
                    adj += 1
                if col_idx < WIDTH - 1:
                    if newlines[row_idx + 1][col_idx + 1] == "#":
                        adj += 1

            if col == "L" and adj == 0:
                lines[row_idx][col_idx] = "#"
                changed = True
            if col == "#" and adj >= 4:
                lines[row_idx][col_idx] = "L"
                changed = True

    # pprint(lines)

occ = 0
for row in lines:
    for col in row:
        if col == "#":
            occ += 1
print(occ)

# Part Two
lines = []
with open("input11.txt") as f:
    for line in f:
        lines.append(list(line.strip()))


changed = True
while changed:
    changed = False
    newlines = [row[:] for row in lines[:]]
    for row_idx, row in enumerate(newlines):
        for col_idx, col in enumerate(row):
            if col == ".": continue
            adj = 0
            # 1
            for x, y in zip(range(row_idx - 1, -1, -1), range(col_idx - 1, -1, -1)):

                if newlines[x][y] == "#":
                    adj += 1
                    break
                elif newlines[x][y] == "L":
                    break

            # 2
            for x, y in zip(range(row_idx - 1, -1, -1), repeat(col_idx)):

                if newlines[x][y] == "#":
                    adj += 1
                    break
                elif newlines[x][y] == "L":
                    break

            # 3
            for x, y in zip(range(row_idx - 1, -1, -1), range(col_idx + 1, WIDTH)):

                if newlines[x][y] == "#":
                    adj += 1
                    break
                elif newlines[x][y] == "L":
                    break

            # 4
            for x, y in zip(repeat(row_idx), range(col_idx - 1, -1, -1)):

                if newlines[x][y] == "#":
                    adj += 1
                    break
                elif newlines[x][y] == "L":
                    break

            # 6
            for x, y in zip(repeat(row_idx), range(col_idx + 1, WIDTH)):

                if newlines[x][y] == "#":
                    adj += 1
                    break
                elif newlines[x][y] == "L":
                    break

            # 7
            for x, y in zip(range(row_idx + 1, HEIGHT), range(col_idx - 1, -1, -1)):

                if newlines[x][y] == "#":
                    adj += 1
                    break
                elif newlines[x][y] == "L":
                    break

            # 8
            for x, y in zip(range(row_idx + 1, HEIGHT), repeat(col_idx)):

                if newlines[x][y] == "#":
                    adj += 1
                    break
                elif newlines[x][y] == "L":
                    break

            # 9
            for x, y in zip(range(row_idx + 1, HEIGHT), range(col_idx + 1, WIDTH)):

                if newlines[x][y] == "#":
                    adj += 1
                    break
                elif newlines[x][y] == "L":
                    break

            if col == "L" and adj == 0:
                lines[row_idx][col_idx] = "#"
                changed = True
            if col == "#" and adj >= 5:
                lines[row_idx][col_idx] = "L"
                changed = True

    # pprint(lines)
    # print()
occ = 0
for row in lines:
    for col in row:
        if col == "#":
            occ += 1
print(occ)
