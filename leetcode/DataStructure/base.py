class StackBase:
    # push, pop, peek, get_size, is_empty
    def push(self):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError


class QueueBase:
    # enqueue, dequeue, get_front, get_size, is_empty
    def enqueue(self):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def get_front(self):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError


class SetBase:
    def add(self, e):
        raise NotImplementedError

    def remove(self, e):
        raise NotImplementedError

    def contains(self, e):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError


class MapBase:
    def add(self, key, value):
        raise NotImplementedError

    def remove(self, key):
        raise NotImplementedError

    def contains(self, key):
        raise NotImplementedError

    def getter(self, key):
        raise NotImplementedError

    def setter(self, key, value):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError


class UF:
    def is_connected(self, p, q):
        raise NotImplementedError

    def union_elements(self, p, q):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

        