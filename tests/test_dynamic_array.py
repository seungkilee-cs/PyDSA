import unittest
from src.dynamic_array import DynamicArray

class TestDynamicArray(unittest.TestCase):
    def setUp(self):
        self.arr = DynamicArray()

    def test_init(self):
        self.assertEqual(len(self.arr), 0)
        self.assertEqual(self.arr.capacity, 10)

    def test_append(self):
        self.arr.append(1)
        self.assertEqual(len(self.arr), 1)
        self.assertEqual(self.arr[0], 1)

    def test_getitem(self):
        self.arr.append(1)
        self.arr.append(2)
        self.assertEqual(self.arr[0], 1)
        self.assertEqual(self.arr[1], 2)
        with self.assertRaises(IndexError):
            _ = self.arr[2]

    def test_len(self):
        self.assertEqual(len(self.arr), 0)
        self.arr.append(1)
        self.assertEqual(len(self.arr), 1)

    def test_insert(self):
        self.arr.append(1)
        self.arr.append(3)
        self.arr.insert(1, 2)
        self.assertEqual(len(self.arr), 3)
        self.assertEqual(self.arr[1], 2)

    def test_remove(self):
        self.arr.append(1)
        self.arr.append(2)
        self.arr.append(3)
        self.arr.remove(2)
        self.assertEqual(len(self.arr), 2)
        self.assertEqual(self.arr[1], 3)

    def test_pop(self):
        self.arr.append(1)
        self.arr.append(2)
        popped = self.arr.pop()
        self.assertEqual(popped, 2)
        self.assertEqual(len(self.arr), 1)

    def test_clear(self):
        self.arr.append(1)
        self.arr.append(2)
        self.arr.clear()
        self.assertEqual(len(self.arr), 0)

    def test_index(self):
        self.arr.append(1)
        self.arr.append(2)
        self.arr.append(3)
        self.assertEqual(self.arr.index(2), 1)
        with self.assertRaises(ValueError):
            self.arr.index(4)

    def test_iter(self):
        self.arr.append(1)
        self.arr.append(2)
        self.arr.append(3)
        self.assertEqual(list(self.arr), [1, 2, 3])

    def test_capacity_increase(self):
        for i in range(11):
            self.arr.append(i)
        self.assertGreater(self.arr.capacity, 10)
        self.assertEqual(len(self.arr), 11)

    def test_negative_indexing(self):
        self.arr.append(1)
        self.arr.append(2)
        self.assertEqual(self.arr[-1], 2)
        self.assertEqual(self.arr[-2], 1)

if __name__ == '__main__':
    unittest.main()
