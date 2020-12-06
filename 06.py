answers = []
with open("input06.txt") as f:
    ans = set('')
    for line in f:
        line = line.strip()
        if not line:
            answers.append(ans)
            ans = set('')
        else:
            ans = ans.union(set(line))

ans = ans.union(set(line))
answers.append(ans)

print(sum([len(a) for a in answers ]))

answers = []
with open("input06.txt") as f:
    ans = set('abcdefghijklmnopqrstuvwxyz')
    for line in f:
        line = line.strip()
        if not line:
            answers.append(ans)
            ans = set('abcdefghijklmnopqrstuvwxyz')
        else:
            ans = ans.intersection(set(line))

ans = ans.intersection(set(line))
answers.append(ans)

print(sum([len(a) for a in answers ]))