class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def index(self, item):
        current = self.head
        index = 0
        while current:
            if current.data == item:
                return index
            current = current.next
            index += 1
        raise ValueError(f"{item} not found in the list")

    def pop(self, index=None):
        if self.is_empty():
            raise IndexError("pop from empty list")

        if index is None:
            index = self.size() - 1

        if index < 0 or index >= self.size():
            raise IndexError("pop index out of range")

        if index == 0:
            popped_item = self.head.data
            self.head = self.head.next
            return popped_item
        else:
            current = self.head
            prev = None
            count = 0
            while count < index:
                prev = current
                current = current.next
                count += 1
            popped_item = current.data
            prev.next = current.next
            return popped_item

    def insert(self, index, item):
        if index < 0 or index > self.size():
            raise IndexError("insert index out of range")

        if index == 0:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            count = 0
            while count < index:
                prev = current
                current = current.next
                count += 1
            new_node = Node(item)
            prev.next = new_node
            new_node.next = current

    def slice(self, start, stop):
        if start < 0 or stop < 0 or start > stop or start >= self.size() or stop > self.size():
            raise ValueError("Invalid slice parameters")

        sliced_list = UnorderedList()
        current = self.head
        count = 0
        while count < start:
            current = current.next
            count += 1

        while count < stop:
            sliced_list.append(current.data)
            current = current.next
            count += 1

        return sliced_list

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __str__(self):
        items = []
        current = self.head
        while current:
            items.append(str(current.data))
            current = current.next
        return " -> ".join(items)


my_list = UnorderedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
print(my_list)
print(my_list.index(3))
my_list.pop(2)
print(my_list)
my_list.insert(2, 3)
print(my_list)
sliced = my_list.slice(1, 3)
print(sliced)
