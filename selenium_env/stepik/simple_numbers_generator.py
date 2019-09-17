import itertools


def primes():
    x = 2
    while True:
        if x == 2:
            yield x
            x += 1
            continue
        elif x == 3:
            yield x
            x += 1
            continue
        elif x % 2 != 0 and x % 3 != 0:
            yield x
            x += 1
        elif x > 9 and x % 5 != 0
        x += 1


print(list(itertools.takewhile(lambda x: x <= 99, primes())))