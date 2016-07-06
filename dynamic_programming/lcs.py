import unittest

"""
Given a sequence X = <x1, x2, ..., xm>, another sequence Z = <z1, z2, ..., zk> is 
a subsequence of X if there exists a strictly increasing sequence <i1, i2, ..., ik> 
of indices of X such that for all j = 1, 2, ..., k, holds xij = zj.

Given two sequences X and Y, a sequence Z is a common subsequence of X and Y if Z is 
a subsequence of both X and Y . 

The longest-common-subsequence problem. Given two sequences X = <x1, x2, ..., xm> 
and Y = <y1, y2, ..., yn>, find a maximum length common subsequence of X and Y.
"""

def lcs(X, Y):
  pass

class Tests(unittest.TestCase):
  def test_motivational(self):
    self.assertEqual(lcs(list('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'),
                         list('GTCGTTCGGAATGCCGTTGCTCTGTAAA')),
                         list('GTCGTCGGAAGCCGGCCGAA'))

if __name__ == '__main__':
  unittest.main()