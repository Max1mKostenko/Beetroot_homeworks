class Mathematician:
    def square_nums(self, _list: list):
        return [i**2 for i in _list]

    def remove_positives(self, _list: list):
        return [i for i in _list if i < 1]

    def filter_leaps(self, _list: list):
        return [i for i in _list if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)]


math = Mathematician()
print(math.square_nums([7, 11, 5, 4]))
print(math.remove_positives([26, -11, -8, 13, -90]))
print(math.filter_leaps([2001, 1884, 1995, 2003, 2020]))
