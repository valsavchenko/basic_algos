"""
T. H. Cormen et. al. - Introduction to Algorithms, 3rd edition, ISBN 978-0262033848
2.3.1 The divide-and-conquer approach (p. 30)

The merge sort algorithm closely follows the divide-and-conquer paradigm.
Intuitively, it operates as follows:
Divide: Divide the n-element sequence to be sorted into two subsequences of n=2 elements each.
Conquer: Sort the two subsequences recursively using merge sort.
Combine: Merge the two sorted subsequences to produce the sorted answer.
"""

import unittest
import itertools

def merge_sort(array):
    """
    Sorts supplied array in-place in O(NlgN) time

    Parameters
    ----------
    array : list
        An array to sort

    Returns
    -------
        Nothing
    """
    total = len(array)

    chunk = 1
    while chunk < total:
        # Merge adjacent singles, pairs, 4-tuples, etc bottom-up, in-place 
        for position in range(0, total, 2 * chunk):
            left = position # Pick a beginning of the left half
            right = position + chunk # Pick a beginning of the right half
            insert = position # Output results at the left half
            end = min(position + 2 * chunk, total) # Interrupt at an end of shortened right halves
            if right == end:
                # Skip, if the right half is practically empty
                continue

            while not (left == right == insert):
                if array[left] <= array[right]:
                    # Put an element from the left-ish half at a final position
                    array[insert], array[left] = array[left], array[insert]

                    if left == insert:
                        # Advance the left-ish half, if it is still within original partition
                        left = left + 1
                    else:
                        # In case there is not enough space to chain the current left-ish,
                        # shift the whole pack of the left-ish elements at the right half
                        # to provide some room for the new-bee
                        l = array[left]
                        for s in range(left, right - 1):
                           array[s] = array[s + 1]
                        array[right - 1] = l

                    if right == insert:
                        # Advance the right-ish half
                        right = right + 1
                else:
                    # Put an element from the right-ish half at a final position
                    array[insert], array[right] = array[right], array[insert]

                    if left == insert:
                        # Head the left-ish half at the vacant position at the right-ish half
                        left = right

                    # Advance the right-ish half
                    right = right + 1
                    if right == end:
                        # Re-establish the halves in case the right one is exhausted
                        right = left
                        left = insert + 1

                insert = insert + 1 # Advance the output position

        chunk = 2 * chunk

if __name__ == '__main__':
    class MergeSort(unittest.TestCase):
        def __is_sorted(self, array):
            decision = all([e <= ne for e, ne in zip(array, array[1:])])
            return decision

        def test_4_merge_sample(self):
            array = [2, 4, 5, 7, 1, 2, 3, 6]
            merge_sort(array)
            self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_4_merge_gggg(self):
            array = [6, 7, 8, 9, 1, 2, 3, 4]
            merge_sort(array)
            self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_4_merge_llgg(self):
            array = [1, 2, 7, 8, 3, 4, 5, 6]
            merge_sort(array)
            self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_4_merge_total_llll(self):
            array = [1, 2, 3, 4, 5, 6, 7, 8]
            merge_sort(array)
            self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_4_merge_lglg(self):
            array = [1, 4, 5, 8, 2, 3, 6, 7]
            merge_sort(array)
            self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_4_merge_llll(self):
            array = [1, 3, 5, 6, 2, 4, 7, 8]
            merge_sort(array)
            self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_4_merge_lllg(self):
            array = [1, 2, 3, 9, 5, 6, 7, 8]
            merge_sort(array)
            self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_4_merge_llxx(self):
            array = [3, 4, 5, 6, 1, 2]
            merge_sort(array)
            self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_01_permutations(self):
            for candidate in itertools.permutations(range(2)):
                array = list(candidate)
                with self.subTest(candidate = candidate, array = array):
                    merge_sort(array)
                    self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_012_permutations(self):
            for candidate in itertools.permutations(range(3)):
                array = list(candidate)
                with self.subTest(candidate = candidate, array = array):
                    merge_sort(array)
                    self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_0123_permutations(self):
            for candidate in itertools.permutations(range(4)):
                array = list(candidate)
                with self.subTest(candidate = candidate, array = array):
                    merge_sort(array)
                    self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_012345_permutations(self):
            for candidate in itertools.permutations(range(6)):
                array = list(candidate)
                with self.subTest(candidate = candidate, array = array):
                    merge_sort(array)
                    self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

        def test_01234567_permutations(self):
            for candidate in itertools.permutations(range(8)):
                array = list(candidate)
                with self.subTest(candidate = candidate, array = array):
                    merge_sort(array)
                    self.assertTrue(self.__is_sorted(array), 'Expecting array to be sorted')

    unittest.main()
