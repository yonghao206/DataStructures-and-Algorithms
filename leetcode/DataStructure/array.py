class Array:
    def __init__(self, arr=None, capacity = 10):
        if isinstance(arr, list):
            self._data = arr[:]
            self._size = len(arr)
            return
        # 这里用的是list，arr的大小用capactiy控制，放入的数据用self._size控制
        self._data = [None] * capacity
        self._size = 0

    def get_size(self):
        return self._size

    def get_capacity(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    def add(self, index, e):
        # 1. valid index 2. size is enough 3. add value 中间加入value时候要从后往前移动出来位置
        # add =  insert: O(n)
        if not 0 <= index <= self._size:
            raise ValueError(
                'add failed. Require index >= 0 and index <= array sise.')

        if self._size == len(self._data):
            if len(self._data) == 0: # 当capacity为0的时候，需要先resize(1)
                self._resize(1)
            self._resize(2 * len(self._data))

        for i in range(self._size, index, -1):
            self._data[i] = self._data[i-1]
        self._data[index] = e
        self._size += 1

    def add_last(self, e):
        self.add(self._size, e)

    def add_first(self, e):
        self.add(0, e)

    def get(self, index):
        if not 0 <= index < self._size:
            raise ValueError('get failed. Index is illegal.')
        return self._data[index]

    def get_last(self):
        return self.get(self._size - 1)

    def get_first(self):
        return self.get(0)

    def set(self, index, e):
        if not 0 <= index < self._size:
            raise ValueError('set failed. Index is illegal.')
        self._data[index] = e

    def contains(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return True
        return False

    def find_index(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return i
        return -1

    def remove(self, index):
        if not 0 <= index < self._size:
            raise ValueError('remove failed. Index is illegal.')
        ret = self._data[index]
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i+1]
        self._size -= 1
        self._data[self._size] = None 
        # resize judge: lazy method; 当self._size为self._data的1/4容量时，进行缩容
        if (self._size == len(self._data) // 4 and len(self._data) // 2 != 0):
            self._resize(len(self._data) // 2)
        return ret

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def remove_element(self, e):
        index = self.find_index(e)
        if index != -1:
            self.remove(index)

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def swap(self, i, j):
        if i < 0 or i >= self._size or j < 0 or j >= self._size:
            raise ValueError('Index is illegal.')
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def __str__(self):
        return str('Array : {}, capacity: {}'.format(self._data[:self._size], self.get_capacity()))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    arr = Array()

    for i in range(10):
        arr.add_last(i)
    print(arr.get_capacity())

    arr.add(1, 'ab')
    print(arr.get_capacity())

    arr.remove_element('ad')
    print(arr)

    arr.add_first(-1)
    print(arr)

    arr.remove_element(8)
    print(arr)

    arr.remove_element('dc')
    print(arr)
