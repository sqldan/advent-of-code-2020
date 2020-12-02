from inputfunctions import intlist, strlist, intline, strline

numbers = intlist("input01.txt")

for i in numbers:
    for j in numbers[1:]:
        if i + j == 2020:
            print(i * j)
