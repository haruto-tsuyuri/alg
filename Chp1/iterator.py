from pprint import pprint


def iterator():
    for num in range(0, 101):
        pprint(f"num = {num} , num id is {id(num)}")
