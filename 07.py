from collections import defaultdict
import re
re_bags = re.compile("\s*(\d+)\s(.*)\sbag")
bags = defaultdict(list)

with open("input07.txt") as f:
    for line in f:
        line = line.strip()
        bag, con = line.split(" bags contain ")
        if con == "no other bags.":
            bags[bag] = []
        else:
            contains = con.split(",")
            for c in contains:
                m = re_bags.match(c)
                nr, color = m.groups()
                bags[bag].append((int(nr), color))

valid_bags = set(["shiny gold"])
found = True
while found:
    found = False
    for key in bags.keys():
        for valid in list(valid_bags):
            if valid in [bag for nr, bag in bags[key]]:
                if key not in valid_bags:
                    valid_bags.add(key)
                    found = True

valid_bags.remove("shiny gold")
print("answer 1:", len(valid_bags))

costs = {}
while len(bags) > 0:
    for k, v in bags.items():
        if set(bag for nr, bag in v).issubset(costs):
            tot = 0
            for nr, bag in v:
                tot += (nr * costs[bag]) + nr
            costs[k] = tot

    for k in costs:
        if k in bags:
            del bags[k]

print("answer 2:", costs['shiny gold'])