from random import randint as rand
import json


def in_range(start, stop, step):
    _list = yield list(({str(i): rand(1, 100)} for i in range(start, stop, step)))


json_list = in_range(1, 21, 1)

for data in json_list:
    print(data)


    def write_to_json(json_file):
        json_object = json.dumps(data, indent=4)
        with open(json_file, "w") as file:
            file.write(json_object)


    write_to_json("file_task_2.json")
