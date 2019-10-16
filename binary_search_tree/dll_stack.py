from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Stack:  # FILO
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Same because we are adding and removing from the end
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = self.storage.__len__()

    def pop(self):
        if not self.storage.head:
            return None
        value = self.storage.tail.value
        self.storage.remove_from_tail()
        self.size = self.storage.__len__()
        return value

    def len(self):
        return self.size