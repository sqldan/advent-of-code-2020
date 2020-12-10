from itertools import combinations, accumulate
from inputfunctions import intlist
numbers = intlist("input09.txt")

preamble = 25
N = 0 # number to look for


def issum(numbers, N):
    return N in [sum(c) for c in combinations(numbers, 2)]


def contiguous(numbers, N):
    for idx, tot in enumerate(accumulate(numbers)):
        if tot == N:
            return min(numbers[:idx]) + max(numbers[:idx])
    return None


for i in range(len(numbers)):
    if not issum(numbers[i:preamble + i], numbers[preamble + i]):
        N = numbers[preamble + i]
        print(N)
        break

for i in range(len(numbers)):
    if answer := contiguous(numbers[i:], N):
        print(answer)
        break