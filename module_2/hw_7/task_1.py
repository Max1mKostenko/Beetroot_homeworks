from string import ascii_lowercase as alphabet


def with_index(iterable, start=0):
    for number, letter in enumerate(iterable, start):
        yield f"{number}: {letter}"


for i in with_index(iterable=list(alphabet), start=1):
    print(i)
