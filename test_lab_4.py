import unittest
from lab_4 import quicksort, parallel_quicksort


class TestQuickSort(unittest.TestCase):

    def test_empty_list(self):
        arr = []
        expected = []
        self.assertEqual(quicksort(arr), expected)
        self.assertEqual(parallel_quicksort(arr, 1), expected)

    def test_one_element(self):
        arr = [5]
        expected = [5]
        self.assertEqual(quicksort(arr), expected)
        self.assertEqual(parallel_quicksort(arr, 1), expected)

    def test_unsorted_list(self):
        arr = [5, 2, 9, 1, 7]
        expected = [1, 2, 5, 7, 9]
        self.assertEqual(quicksort(arr), expected)
        self.assertEqual(parallel_quicksort(arr, 1), expected)
        self.assertEqual(parallel_quicksort(arr, 2), expected)

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(quicksort(arr), expected)
        self.assertEqual(parallel_quicksort(arr, 1), expected)

    def test_duplicates(self):
        arr = [4, 2, 4, 1, 2]
        expected = [1, 2, 2, 4, 4]
        self.assertEqual(quicksort(arr), expected)
        self.assertEqual(parallel_quicksort(arr, 1), expected)
        self.assertEqual(parallel_quicksort(arr, 2), expected)


if __name__ == '__main__':
    unittest.main()