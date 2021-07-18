"""
Given a sequence X = <x1, x2, ..., xm>, another sequence Z = <z1, z2, ..., zk> is a subsequence of X if there exists
a strictly increasing sequence <i1, i2, ..., ik> of indices of X such that for all j = 1, 2, ..., k,
holds Xi_j = Zj.
For example, Z = <B, C, D, B> is a subsequence of X = <A, B, C, B, D, A, B> with corresponding index sequence
<2, 3, 5, 7>.

Given two sequences X and Y, a sequence Z is a common subsequence of X and Y if Z is a subsequence of both X and Y.
For example, if X = <A, B, C, B, D, A, B> and Y = <B, D, C, A, B, A>, the sequence <B, C, A> is a common subsequence
of both X and Y.

The longest-common-subsequence problem. Given two sequences X = <x1, x2, ..., xm> and Y = <y1, y2, ..., yn>, find
a maximum length common subsequence of X and Y.
For example, if X = <A, B, C, B, D, A, B> and Y = <B, D, C, A, B, A>, both sequences <B, C, B, A> and <B, D, A, B>
are LCS of X and Y? since X and Y have no common subsequence of length 5 or greater.
"""

import unittest


def unwind_lcs(sequence_x, sequence_y, lcs_ij):
    i = len(sequence_x)
    assert (i == len(lcs_ij) - 1)
    j = len(sequence_y)
    assert (j == len(lcs_ij[0]) - 1)

    lcs = []
    while 0 < i and 0 < j:
        # If the last elements of the Xi and the Yj prefixes match, add it at the beginning of the LCS
        # Otherwise keep shortening appropriate prefixes to move on to the next element of the LCS
        if sequence_x[i - 1] == sequence_y[j - 1]:
            lcs.insert(0, sequence_x[i - 1])
            i = i - 1
            j = j - 1
        elif lcs_ij[i][j] == lcs_ij[i - 1][j]:
            i = i - 1
        else:
            assert lcs_ij[i][j] == lcs_ij[i][j - 1]
            j = j - 1
    assert lcs_ij[len(sequence_x)][len(sequence_y)] == len(lcs)

    return lcs


def find_lcs(sequence_x, sequence_y):
    # Prepare a matrix to express an LCS of the first i elements of X sequence and the first j elements of Y sequence
    # through the prefix sequences of X/Y of smaller sizes
    m = len(sequence_x)
    n = len(sequence_y)
    lcs_ij = [[0 for j in range(n + 1)] for i in range(m + 1)]

    # Fill the matrix in a bottom up fashion: the X1 prefix against the Y1, Y2, ..., Yn prefixes, then the X2 prefix
    # against all the prefix sequences of Y, etc. until the Xm prefix is examined
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if sequence_x[i - 1] == sequence_y[j - 1]:
                # If both the Xi prefix and the Yj prefix have the same element at their tails, then the Xi-1 prefix and
                # the Yj-1 prefix must shared the very same LCS
                lcs_ij[i][j] = lcs_ij[i - 1][j - 1] + 1
            elif lcs_ij[i][j - 1] <= lcs_ij[i - 1][j]:
                # If tails of the Xi prefix and the Yj prefix mismatch and their LCS does not contain the tail of X,
                # then their LCS must match an LCS of the Xi-1 and the Yj
                lcs_ij[i][j] = lcs_ij[i - 1][j]
            else:
                # Complimentary to the previous case, an LCS must match an LCS of the Xi and the Yj-1
                assert lcs_ij[i - 1][j] < lcs_ij[i][j - 1]
                lcs_ij[i][j] = lcs_ij[i][j - 1]

    # Reconstruct an LCS for the initial sequences
    return unwind_lcs(sequence_x, sequence_y, lcs_ij)


def find_lcs_recursively(sequence_x, sequence_y):
    # Use the same observation as for find_lcs, but this time compute LCSes of prefixes recursively with memoization

    # Prepare a matrix for LCSes of prefixes
    m = len(sequence_x)
    n = len(sequence_y)
    unknown_lcs_length = -1
    lcs_ij = [[unknown_lcs_length for j in range(n + 1)] for i in range(m + 1)]

    # Compute an LCS of a Xi prefix and a Yj prefix
    def find_lcs_recursively_impl(i, j):
        # Wrap up if either prefix has a zero length
        if i == 0 or j == 0:
            return 0

        # Wrap up if an LCS for the prefixes is already known
        if lcs_ij[i][j] != unknown_lcs_length:
            return lcs_ij[i][j]

        # Dive one recursion level below to compose an LCS for the Xi prefix and the Yj prefix from the smaller prefixes
        if sequence_x[i - 1] == sequence_y[j - 1]:
            lcs_ij[i][j] = find_lcs_recursively_impl(i - 1, j - 1) + 1
        else:
            lcs_ij[i][j] = max(find_lcs_recursively_impl(i, j - 1),
                               find_lcs_recursively_impl(i - 1, j))

        # Supply an LCS of the prefixes
        return lcs_ij[i][j]

    find_lcs_recursively_impl(m, n)

    # Reconstruct an LCS for the initial sequences
    return unwind_lcs(sequence_x, sequence_y, lcs_ij)


class Tests(unittest.TestCase):
    def test_motivational_dna(self):
        x = list('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA')
        y = list('GTCGTTCGGAATGCCGTTGCTCTGTAAA')
        expected_lcs = list('GTCGTCGGAAGCCGGCCGAA')

        lcs = find_lcs(x, y)
        lcs_recursively = find_lcs_recursively(x, y)
        self.assertTrue(lcs == lcs_recursively == expected_lcs)

    def test_motivational_lcs_example(self):
        x = list('ABCBDAB')
        y = list('BDCABA')
        expected_lcs = list('BCBA')

        lcs = find_lcs(x, y)
        lcs_recursively = find_lcs_recursively(x, y)
        self.assertTrue(lcs == lcs_recursively == expected_lcs)

    def test_indexing(self):
        x = list('ABC')
        y = list('AC')
        expected_lcs = list('AC')

        lcs = find_lcs(x, y)
        lcs_recursively = find_lcs_recursively(x, y)
        self.assertTrue(lcs == lcs_recursively == expected_lcs)

    def test_15_4_1(self):
        x = list('10010101')
        y = list('010110110')
        expected_lcs = list('100110')

        lcs = find_lcs(x, y)
        lcs_recursively = find_lcs_recursively(x, y)
        self.assertTrue(lcs == lcs_recursively == expected_lcs)


if __name__ == '__main__':
    unittest.main()
