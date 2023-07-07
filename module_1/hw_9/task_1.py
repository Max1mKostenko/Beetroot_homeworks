def oops():
    raise IndexError("Hello World")


def oops_2():
    raise KeyError("Hello World")


def oops_3():
    try:
        # oops()
        oops_2()
    except IndexError:
        return "Index Error)"
    
    # except KeyError:
    #     return "Key Error("


print(oops_3())
