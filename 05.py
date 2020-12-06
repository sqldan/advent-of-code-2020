lines = []
with open("input05.txt") as f:
    for line in f:
        lines.append(line)

values = [64, 32, 16, 8, 4, 2, 1, 4, 2, 1]

seat_ids = []
for line in lines:
    rows = seats = 0
    for i, c in enumerate(line):
        if c == "B":
            rows += values[i]
        if c == "R":
            seats += values[i]

    seat_ids.append(rows * 8 + seats)

answer1 = max(seat_ids)
answer2 = 0
for x in range(7, answer1):
    if x not in seat_ids:
        answer2 = x
        break

print(answer1, answer2)