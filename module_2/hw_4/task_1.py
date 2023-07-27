class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class Student(Person):
    def __init__(self, name, surname, age, school_classroom, classroom, **grades):
        super().__init__(name, surname, age)
        self.school_classroom = school_classroom
        self.classroom = classroom
        self.grades = grades

    def info_of_student(self):
        return f"\n{'info of student'.upper()}:" \
               f"\nName: {self.name} " \
               f"\nSurname: {self.surname}" \
               f"\nAge: {self.age}" \
               f"\nSchool class: {self.school_classroom}" \
               f"\nClassroom: {self.classroom}" \
               f"\nAn average grade is equal: {round(sum(self.grades.values())/len(self.grades), 2)}"


class Teacher(Person):
    def __init__(self, name, surname, age, quantity_of_classes, own_classroom):
        super().__init__(name, surname, age)
        self.quantity_of_class = quantity_of_classes
        self.own_classroom = own_classroom

    def info_of_teacher(self):
        return f"""\n{'info of teacher'.upper()}:
Name: {self.name}
Surname: {self.surname}
Age: {self.age}
Quantity of classes: {self.quantity_of_class}
Own classroom: {self.own_classroom}"""
    # return f"\nInfo of teacher: {self.name} {self.surname}" \
    #        f"Name: {self.name} " \
    #        f"Surname: {self.surname}" \
    #        f"\nAge: {self.age} y.o." \
    #        f"\nQuantity of classes: {self.quantity_of_class}" \
    #        f"\nOwn classroom: {self.own_classroom}"


student = Student("Maxim", "Kostenko", 15, "9-C", 214, mathematics=10, science=7, history=10, english=9,
                  computer_Science=9, physical_Education=9, ukrainian=10)
teacher = Teacher("Elena", "Dvirska", 49, 14, "9-C")
print(student.info_of_student())
print(teacher.info_of_teacher())
