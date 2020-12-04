from pprint import pprint
import re
lines = []
with open("input04.txt") as f:
    pp = {}
    for line in f:
        line = line.strip()
        if not line:
            lines.append(pp)
            pp = {}
        else:
            pairs = line.split()
            items = [x.split(":") for x in pairs]
            pp = pp | {x: y for x, y in items}

if pp:
    lines.append(pp)

answer1 = answer2 = 0
fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
re_hgt = re.compile("^(\d+)(cm|in)$")
re_hcl = re.compile("^#[0-9a-f]{6}$")
re_pid = re.compile("^[0-9]{9}$")
for pp in lines:
    if fields.issubset(set(pp)):
        answer1 += 1
        if not 1920 <= int(pp['byr']) <= 2002:
            continue
        if not 2010 <= int(pp['iyr']) <= 2020:
            continue
        if not 2020 <= int(pp['eyr']) <= 2030:
            continue
        if m:= re_hgt.match(pp['hgt']):
            hgt, hgt_type = m.groups()
            if hgt_type == "cm" and not 150 <= int(hgt) <= 193:
                continue
            if hgt_type == "in" and not 59 <= int(hgt) <= 76:
                continue
        else:
            continue
        if not re_hcl.match(pp['hcl']):
            continue
        if not pp['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn' ,'hzl', 'oth'):
            continue
        if not re_pid.match(pp['pid']):
            continue

        answer2 += 1

print(answer1, answer2)
