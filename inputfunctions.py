def intlist(filename: str) -> list[int]:
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(int(line))
    return numbers


def strlist(filename: str) -> list[str]:
    strings = []
    with open(filename) as f:
        for line in f:
            strings.append(line.strip())
    return strings


def intline(filename: str) -> list[int]:
    with open(filename) as f:
        line = f.readline()
        return [int(l) for l in line.split(",")]


def strline(filename: str) -> list[str]:
    with open(filename) as f:
        line = f.readline()
        return [s.strip() for s in line.split(",")]
