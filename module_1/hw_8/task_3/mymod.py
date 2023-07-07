def count_of_lines(name):
    with open(name, "r") as file:
        return len(file.readlines())


def count_of_chars(name):
    with open(name, "r") as file_2:
        return len(file_2.read())


def test(name):
    with open(name, "r") as file_3:
        file_3.seek(0)
        lines = count_of_lines(name)
        file_3.seek(0)
        chars = count_of_chars(name)
    print(lines)
    print(chars)
