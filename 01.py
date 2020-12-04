from inputfunctions import intlist, strlist, intline, strline

numbers = intlist("input01.txt")


def answer1():
    for i in numbers:
        if 2020 - i in numbers:
            return i * (2020 - i)


def answer2():
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if (2020 - numbers[i] - numbers[j]) in numbers:
                return numbers[i] * numbers[j] * (2020 - numbers[i] - numbers[j])

print(answer1(), answer2())
