class Stack:
    def __init__(self):
        self.items = [1, 2, 3, 4, "e", "b", "c", "s"]

    def get_from_stack(self):
        items = self.items

        """
        # First variant
        """

        if "e" in items:
            print(items)
            print(items.pop(items.index("e")))
        else:
            print(items)
            raise ValueError("Element 'e' not in a stack")
        print(items)

        """
        Second variant
        """

        # for index, item in enumerate(items):
        #     if item == "e":
        #         print(items)
        #         print(items.pop(index))
        #         break
        #     elif "e" not in items:
        #         print(items)
        #         raise ValueError("Element 'e' not in a stack")
        # print(items)


stack = Stack()
stack.get_from_stack()
