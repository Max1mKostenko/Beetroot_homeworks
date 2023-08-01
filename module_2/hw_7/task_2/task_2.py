from random import randint as rand
# import json


def in_range(start, stop, step):
    _list = list(({i: rand(1, 100)} for i in range(start, stop, step)))
    yield _list


for i in in_range(1, 21, 1):
    print(i)


# json_file = "file_task_2.json"
# with open(json_file, "r") as file:
#     data = json.load(file)
# data.extend(list(({i: rand(1, 100)} for i in range(1, 21, 1))))
# with open(json_file, "w") as file:
#     json.dump(data, file, indent=4)
