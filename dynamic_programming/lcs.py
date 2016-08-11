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
  m = len(X)
  n = len(Y)
  c = [[0 for j in range(n+1)] for i in range(m+1)]
  b = [[(0, 0) for j in range(n)] for i in range(m)]

  WN = (-1, -1)
  N = (-1, 0)
  W = (0, -1)

  for i in range(1, m+1):
    for j in range(1, n+1):
      if X[i-1] == Y[j-1]:
        c[i][j] = c[i-1][j-1] + 1
        b[i-1][j-1] = WN
      elif c[i-1][j] >= c[i][j-1]:
        c[i][j] = c[i-1][j]
        b[i-1][j-1] = N
      elif c[i][j] == c[i][j-1]:
        b[i-1][j-1] = W

  print(c, b)

  i = m-1
  j = n-1
  seq = []
  while i >= 0 and j >= 0:
    print(i, j)
    if X[i] == Y[j]:
      seq.insert(0, X[i])
    ii = i
    jj = j
    i += b[ii][jj][0]
    j += b[ii][jj][1]
    assert(ii != i or jj != j)

  return seq

class Tests(unittest.TestCase):
#  def test_motivational_dna(self):
#    self.assertEqual(lcs(list('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'),
#                         list('GTCGTTCGGAATGCCGTTGCTCTGTAAA')),
#                         list('GTCGTCGGAAGCCGGCCGAA'))
  def test_motivational_lcs_example(self):
    self.assertEqual(lcs(list('ABCBDAB'), list('BDCABA')), list('BCBA'))

  def test_indexing(self):
    self.assertEqual(lcs(list('ABC'), list('AC')), list('AC'))

if __name__ == '__main__':
  unittest.main()