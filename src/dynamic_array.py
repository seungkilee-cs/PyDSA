class DynamicArray:
    def __init__(self, capacity=10):
        """Initialize the dynamic array with a given capacity."""
        self.arr = [None] * capacity
        self.len = 0
        self.capacity = capacity

    def __len__(self):
        """Return the number of elements in the array."""
        for i, e in enumerate(self.arr):
            if e == None:
                return i
            return 0

    def __getitem__(self, index):
        """Get the element at the specified index."""
        for i, e in enumerate(self.arr):
            if i == index:
                return e
            return -1

    def append(self, item):
        """Add an item to the end of the array."""
        if self.len == len(self.arr):
            self.increase_capacity()
        self.arr[self.len] = item
        self.len += 1

    def increase_capacity(self, multiplier=2):
        """Double the Capacity of an array"""
        self.capacity *= multiplier
        scale = [None] * (self.capacity * multiplier-1)
        self.arr = self.arr + scale

    def insert(self, index, item):
        """Insert an item at the specified index."""
        if index > self.capacity:
            while index > self.capacity:
                self.increase_capacity()
            self.arr[index]

    def remove(self, item):
        """Remove the first occurrence of the item from the array."""
        pass

    def pop(self, index=-1):
        """Remove and return the item at the specified index."""
        if index > self.len:
            return -1
        res = self.arr[index]
        self.len-=1
        self.arr[index] = None
        return res

    def clear(self):
        """Remove all items from the array."""
        for i in range(self.len):
            self.arr[i] = None

    def index(self, item):
        """Return the index of the first occurrence of the item."""
        for i,e in enumerate(self.arr):
            if e == item:
                return i
        return -1

    def __iter__(self):
        """Return an iterator for the array."""
        pass
