from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.storage = {}
        self.order = DoublyLinkedList()
        self.size = 0
        self.limit = limit

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        # Get the item or handle none
        if key in self.storage and self.size > 0:
            get_node = self.storage[key]  # node = value
            self.order.move_to_end(get_node)
            return get_node.value[1]
        return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # If key already exists, overwrite the old value and move to end
        if key in self.storage:
            set_node = self.storage[key]
            set_node.value = (key, value)
            self.order.move_to_end(set_node)
            return

        # if cache is full, remove oldest entry in the dict and DLL
        if self.size >= self.limit:
            oldest_node = self.order.head
            del self.storage[oldest_node.value[0]]
            self.order.remove_from_head()  # delete oldest node
            self.size -= 1

        # add to dictionary and DLL if not already in them
        self.order.add_to_tail((key, value))
        self.storage[key] = self.order.tail
        self.size += 1
