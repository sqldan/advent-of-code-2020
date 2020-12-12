facing = "E"
directions = ["E", "S" ,"W", "N"]
lines = []
with open("test.txt") as f:
    for line in f:
        line = line.strip()
        lines.append((line[0], int(line[1:])))

x = y = 0
for direction, move in lines:
    if direction == "F":
        direction = facing
    if direction == "N":
        y += move
    if direction == "E":
        x += move
    if direction == "S":
        y -= move
    if direction == "W":
        x -= move
    if direction == "R":
        facing = directions[(directions.index(facing) + (move // 90)) % 4]
    if direction == "L":
        facing = directions[(directions.index(facing) - (move // 90)) % 4]

print(abs(x) + abs(y))

x = y = 0
wx = 10; wy = 1
for direction, move in lines:
    if direction == "F":
        x += wx * move
        y += wy * move
    if direction == "N":
        wy += move
    if direction == "E":
        wx += move
    if direction == "S":
        wy -= move
    if direction == "W":
        wx -= move
    if direction == "R":
        for _ in range(move // 90):
            wx, wy = wy, wx
            wy *= -1

    if direction == "L":
        for _ in range(move // 90):
            wx, wy = wy, wx
            wx *= -1

print(abs(x) + abs(y))
