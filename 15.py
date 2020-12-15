def find_turn(numbers, target):
    spoken = set(numbers[:-1])
    turn = len(numbers)
    new = numbers[-1]
    previous = {}
    for idx, nr in enumerate(numbers):
        previous[nr] = idx + 1

    while turn != target:
        if new not in spoken:
            spoken.add(new)
            previous[new] = turn
            new = 0
        else:
            temp = previous[new]
            previous[new] = turn
            new = turn - temp
        turn += 1
        numbers.append(new)

    return new

print(find_turn([19,0,5,1,10,13], 2020))
print(find_turn([19,0,5,1,10,13], 30_000_000))