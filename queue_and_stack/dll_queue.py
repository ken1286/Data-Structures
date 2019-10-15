
from doubly_linked_list import DoublyLinkedList
# import sys
# sys.path.append('../doubly_linked_list')


class Queue:  # FIFO
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size = self.storage.__len__()

    def dequeue(self):
        if not self.storage.head:
            return None
        value = self.storage.head.value
        self.storage.remove_from_head()
        self.size = self.storage.__len__()
        return value

    def len(self):
        return self.size
