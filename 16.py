import re
from collections import defaultdict

re_ranges = re.compile("^(.*):.*?(\d+)-(\d+).*?(\d+)-(\d+)$")

ranges = defaultdict(list)
with open("input16.txt") as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        m = re_ranges.match(line)
        name, f1, t1, f2, t2 = m.groups()
        ranges[name].append((int(f1), int(t1)))
        ranges[name].append((int(f2), int(t2)))

    f.readline()
    my_tickets = [int(i) for i in f.readline().strip().split(",")]
    next(f)
    next(f)
    nearby_tickets = []
    for line in f:
        nearby_tickets.append([int(i) for i in line.strip().split(",")])

total_errors = 0
for row in nearby_tickets[:]:
    for nr in row:
        valid = False
        for key, value in ranges.items():
            for low, high in value:
                if low <= nr <= high:
                    valid = True

        if not valid:
            total_errors += nr
            nearby_tickets.remove(row)

print("answer 1:", total_errors)

nearby_tickets = list(zip(*nearby_tickets)) # transpose
remaining_ranges = list(ranges.keys())
positions = {}

while len(remaining_ranges):
    for idx, tickets in enumerate(nearby_tickets):
        found_ranges = remaining_ranges[:]
        for nr in tickets:
            for name in remaining_ranges:
                range_list = ranges[name]
                low1, high1 = range_list[0]
                low2, high2 = range_list[1]
                if not (low1 <= nr <= high1 or low2 <= nr <= high2):
                    found_ranges.remove(name)

        if len(found_ranges) == 1:
            found_range = found_ranges[0]
            positions[idx] = found_range
            remaining_ranges.remove(found_range)

sorted_positions = ([positions[i] for i in sorted(positions.keys())])
total = 1
for idx, nr in enumerate(my_tickets):
    if sorted_positions[idx].startswith("departure"):
        total *= nr
print("answer 2:", total)