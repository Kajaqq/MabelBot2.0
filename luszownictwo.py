import random


def lurczak():
    with open("miejski slownik kurczaka.txt", "r") as f:
        random.seed()
        lines = f.read().split("\n")
        return lines[random.randint(0, (len(lines) - 1))]
