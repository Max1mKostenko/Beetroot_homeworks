def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(arg):
            if type(arg) == type_ and len(arg) <= max_length and all(i in arg for i in contains):
                return func(arg)
            else:
                return False
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def function(name: str):
    return f"Your string: {name}"


print(function('S@SH05'))
print(function('johndoe05@gmail.com'))
