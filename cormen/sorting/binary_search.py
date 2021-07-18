"""
T. H. Cormen et. al. - Introduction to Algorithms, 3rd edition, ISBN 978-0262033848
Exercises 2.3-5 (p. 39)

Referring back to the searching problem (see Exercise 2.1-3), observe that if the
sequence A is sorted, we can check the midpoint of the sequence against and
eliminate half of the sequence from further consideration. The binary search algorithm
repeats this procedure, halving the size of the remaining portion of the
sequence each time. Write pseudocode, either iterative or recursive, for binary
search. Argue that the worst-case running time of binary search is O(lgN).
"""

import unittest

def preventUnordered(searcher):
    def onCall(values, value):
        if not __debug__:
            return searcher(values, value)
        
        for v, nv in zip(values[:-1], values[1:]):
            if nv < v:
                raise ValueError('Values to search among ' + str(values) +
                                 ' are not sorted. The earliest contradiction is between ' +
                                 str(v) + ' and ' + str(nv))
        return searcher(values, value)
    return onCall

@preventUnordered
def search_binary(values, value):
    """
    Performs binary search of given value among ordered values

    Parameters
    ----------
    values : list of int
        Ordered values to search among

    value : int
        A value to search for

    Returns
    -------
    bool
        True if value is among values, False otherwise
    """
    begin = 0
    end = len(values)

    while begin != end:
        middle = int((begin + end) / 2)
        if values[middle] == value:
            return True

        if values[middle] < value:
            begin = middle + 1
        else:
            end = middle

    return False

if __name__ == '__main__':
    class BinarySearch(unittest.TestCase):
        def setUp(self):
            self.motivationalValues = [3, 8, 23, 31, 31, 38, 45, 56]

        def test_unordered_values(self):
            self.assertRaises(ValueError, search_binary, [2534, 123, 345345], 345)

        def test_motivational_in(self):
            n = len(self.motivationalValues)
            self.assertTrue(search_binary(self.motivationalValues,
                            self.motivationalValues[int(n / 3)]))

        def test_motivational_in_challenging_middle(self):
            self.assertTrue(search_binary(self.motivationalValues,
                            self.motivationalValues[-2]))

        def test_motivational_in_last(self):
            self.assertTrue(search_binary(self.motivationalValues,
                            self.motivationalValues[-1]))

        def test_motivational_in_first(self):
            self.assertTrue(search_binary(self.motivationalValues,
                            self.motivationalValues[0]))

        def test_motivational_out(self):
            self.assertFalse(search_binary(self.motivationalValues,
                             self.motivationalValues[0] - 1))

    unittest.main()