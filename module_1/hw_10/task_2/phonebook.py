import json
json_file = "phonebook.json"


def main(input_action):
    try:
        input_action = int(input_action)
        assert 0 < input_action < 10
    except (ValueError, AssertionError):
        return f"\nYour input: '{input_action}', isn't correct!. You should enter only numbers in the range 1 to 9."
    if input_action == 1:
        return add_new_entry(input("Please enter first name of new contact: "),
                             input("Please enter last name of new contact: "),
                             input("Please enter telephone number of length 10 for new contact (like -> 1234567890): "),
                             input("Please enter city of new contact: "),
                             input("Please enter state of new contact (like AL, HI, NY): "))
    elif input_action == 2:
        return search_by_first_name()
    elif input_action == 3:
        return search_by_last_name()
    elif input_action == 4:
        return search_by_full_name()
    elif input_action == 5:
        return search_by_telephone_number()
    elif input_action == 6:
        return search_by_city()
    elif input_action == 7:
        return delete_a_record_for_a_telephone_number()
    elif input_action == 8:
        return update_a_record_for_a_telephone_number()
    elif input_action == 9:
        return quit_a_program()


def add_new_entry(first_name, last_name, telephone, city, state):
    if city.isalpha() and state.isalpha():
        if telephone.isdigit():
            if len(state) == 2:
                if len(telephone) == 10:
                    new_entry = {"first name": first_name.capitalize(),
                                 "last name": last_name.capitalize(),
                                 "telephone": telephone,
                                 "city": city.capitalize(),
                                 "state": state.upper()}
                    with open(json_file, "r") as file:
                        data = json.load(file)
                    with open(json_file, "w") as file:
                        data.append(new_entry)
                        json.dump(data, file, indent=4)
                else:
                    print(f"The length of telephone number: '{telephone}', isn't equal 10!")
            else:
                print(f"The length of state: '{state}', isn't equal 2!")
        else:
            print(f"Your entered telephone number: '{telephone}', should have only numbers!")
    else:
        print(f"Your entered city: '{city}' or state: '{state}'. Should have only letters")


def search_by_first_name():
    with open(json_file, "r") as file:
        data = json.load(file)
        names = [i["first name"] for i in data]
        name = input(f"Please enter someone first name of contact list: {names}\nTo see info about this contact: ")
        if name not in names:
            print(f"Your input: '{name}' isn't valid, the contacts have only these names: {names} ")
        else:
            for i in data:
                if i["first name"] == name:
                    print(f"\nName: {i['first name']}\n"
                          f"Surname: {i['last name']}\n"
                          f"Telephone number: {i['telephone']}\n"
                          f"City: {i['city']}\n"
                          f"State: {i['state']}")


def search_by_last_name():
    with open(json_file, "r") as file:
        data = json.load(file)
        surnames = [i["last name"] for i in data]
        surname = input(f"Please enter someone last name of contact list: {surnames}\nTo see info about this contact: ")
        if surname not in surnames:
            print(f"Your input: '{surname}' isn't valid, the contacts have only these surnames: {surnames} ")
        else:
            for i in data:
                if i["last name"] == surname:
                    print(f"\nName: {i['first name']}\n"
                          f"Surname: {i['last name']}\n"
                          f"Telephone number: {i['telephone']}\n"
                          f"City: {i['city']}\n"
                          f"State: {i['state']}")


def search_by_full_name():
    with open(json_file, "r") as file:
        data = json.load(file)
        full_names = []
        for i in data:
            full_names.append(f"{i['first name']} {i['last name']}")
        full_name = input(f"Please enter someone full name of contact list: "
                          f"{full_names}\nTo see info about this contact: ")
        if full_name not in full_names:
            print(f"Your input: '{full_name}' isn't valid, the contacts have only these full names: {full_names} ")
        else:
            for i in data:
                if i['first name'] == full_name.split(" ")[0] and i["last name"] == full_name.split(" ")[-1]:
                    print(f"\nName: {i['first name']}\n"
                          f"Surname: {i['last name']}\n"
                          f"Telephone number: {i['telephone']}\n"
                          f"City: {i['city']}\n"
                          f"State: {i['state']}")


def search_by_telephone_number():
    with open(json_file, "r") as file:
        data = json.load(file)
        nums = [i["telephone"] for i in data]
        num = input(f"Please enter someone telephone of contact list: {nums}\nTo see info about this contact: ")
        if num not in nums:
            print(f"Your input: '{num}' isn't valid, the contacts have only these numbers: {nums} ")
        else:
            for i in data:
                if i["telephone"] == num:
                    print(f"\nName: {i['first name']}\n"
                          f"Surname: {i['last name']}\n"
                          f"Telephone number: {i['telephone']}\n"
                          f"City: {i['city']}\n"
                          f"State: {i['state']}")


def search_by_city():
    with open(json_file, "r") as file:
        data = json.load(file)
        cities = {i["city"] for i in data}
        city = input(f"Please enter someone city of contact list: {cities}\nTo see info about this contact: ")
        if city not in cities:
            print(f"Your input: '{city}' isn't valid, the contacts have only these cities: {cities} ")
        else:
            for i in data:
                if i["city"] == city:
                    print(f"\nName: {i['first name']}\n"
                          f"Surname: {i['last name']}\n"
                          f"Telephone number: {i['telephone']}\n"
                          f"City: {i['city']}\n"
                          f"State: {i['state']}")


def delete_a_record_for_a_telephone_number():
    with open(json_file, "r") as file:
        data = json.load(file)
        numbs = [i["telephone"] for i in data]
        numb = input(f"Please enter someone telephone number of contact list: {numbs}\nTo delete this contact: ")
        if numb not in numbs:
            print(f"Your input: '{numb}' isn't valid, the contacts have only these numbers: {numbs} ")
        else:
            for i in data:
                if i["telephone"] == numb:
                    data.remove(i)
    with open(json_file, "w") as file:
        file.write(json.dumps(data, indent=4))


def update_a_record_for_a_telephone_number():
    with open(json_file, "r") as file:
        data = json.load(file)
        numbers = [i["telephone"] for i in data]
        number = input(f"Please enter someone telephone number of contact list: {numbers}\n"
                       f"To change info about this contact: ")
        if number not in numbers:
            print(f"Your input: '{number}' isn't valid, the contacts have only these numbers: {numbers} ")
        else:
            for i in data:
                if i["telephone"] == number:
                    name = input("Please enter name of contact: ")
                    surname = input("Please enter surname of contact: ")
                    new_city = input("Please enter city of contact: ")
                    new_state = input("Please enter state of contact (like AL, HI, NY): ")
                    if new_city.isalpha() and new_state.isalpha():
                        if len(new_state) == 2:
                            i["first name"] = name.capitalize()
                            i["last name"] = surname.capitalize()
                            i["city"] = new_city.capitalize()
                            i["state"] = new_state.upper()
                        else:
                            print(f"The length of state: '{new_state}', isn't equal 2!")
                    else:
                        print(f"Your entered city: '{new_city}' or state: '{new_state}'. Should have only letters")
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)


def quit_a_program():
    print("You successfully quit a program!")


main(input("Please enter 1 - (to add new entry)"
           "\n\t\t   / 2 - (to search a contact by first name)"
           "\n\t\t   / 3 - (to search a contact by last name)"
           "\n\t\t   / 4 - (to search a contact by full name)"
           "\n\t\t   / 5 - (to search a contact by telephone number)"
           "\n\t\t   / 6 - (to search a contact by city)"
           "\n\t\t   / 7 - (to delete a record for a given telephone number)"
           "\n\t\t   / 8 - (to update a record for a given telephone number)"
           "\n\t\t   / 9 - (to quit a program): "))
