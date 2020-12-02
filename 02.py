import re

rule1 = rule2 = 0
policy = re.compile("^(\d+)-(\d+)\s([a-z]):\s(.*)$")
with open("input02.txt") as f:
    for line in f:
        m = policy.match(line)
        nr1, nr2, char, password = m.groups()
        nr1, nr2 = int(nr1), int(nr2)

        if nr1 <= password.count(char) <= nr2:
            rule1 += 1

        if (password[nr1 - 1] == char) ^ (password[nr2 - 1] == char):
            rule2 += 1

print(rule1, rule2)
