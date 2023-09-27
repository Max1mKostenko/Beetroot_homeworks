class Stack:
    def __init__(self):
        self.items = [1, 2, 3, 4]

    def vice_versa(self):
        new_list = []
        print(self.items)
        for i in range(len(self.items)):
            new_list.append(self.items.pop())
        print(self.items)
        print(new_list)


stack = Stack()
stack.vice_versa()


