from itertools import chain

search = {
    0: [4, 1, 5],
    1: [[2, 3], [3, 2]],
    2: [[4, 4], [5, 5]],
    3: [[4, 5], [5, 4]],
}

found = {
    4: "a",
    5: "b",
}

def get_rule(rule):
    if rule in found:
        return found[rule]

    # return recurse(rule)


def get_listitems(search_list):
    if len(search_list) == 2:
        items_one = [get_rule(r) for r in search_list[0]]
        items_two = [get_rule(r) for r in search_list[1]]
        items = [items_one, items_two]
        # items = chain(items_one, items_two)
    else:
        items = [get_rule(r) for r in search_list[0]]

    return items


def recurse(rule):
    if rule in found:
        return found[rule]
    else:
        found[rule] = get_listitems(search[rule])
    return found[rule]

print(list(recurse(3)))
