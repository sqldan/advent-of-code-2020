from inputfunctions import intlist, strlist, intline, strline

numbers = intlist("input01.txt")

for i in numbers:
    for j in numbers[1:]:
        for k in numbers[2:]:
            if i + j + k == 2020:
                print(i * j * k)