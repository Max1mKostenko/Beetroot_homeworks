def multiply(num):
    return num * 5


def double(f):
    def result_f(numb):
        return f(numb)
    return result_f


res = double(multiply)
print(res(5))
