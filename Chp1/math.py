from pprint import pprint


def kuku() -> None:
    range1 = range(2, 10)
    range2 = range(1, 10)
    kuku_list = [n1 * n2 for n1 in range1 for n2 in range2]
    pprint(kuku_list)
