import unittest

def construct(X, Y, c):
  i = len(X)
  assert(i == len(c) - 1)
  j = len(Y)
  assert(j == len(c[0]) - 1)

  seq = []
  while i > 0 and j > 0:
    if X[i - 1] == Y[j - 1]:
      seq.insert(0, X[i - 1])
      i = i - 1
      j = j - 1
    elif c[i][j] == c[i - 1][j]:
      i = i - 1
    else:
      j = j - 1
  assert(c[len(X)][len(Y)] == len(seq))

  return seq

def lcs(X, Y):
  """
  Given a sequence X = <x1, x2, ..., xm>, another sequence Z = <z1, z2, ..., zk> is 
  a subsequence of X if there exists a strictly increasing sequence <i1, i2, ..., ik> 
  of indices of X such that for all j = 1, 2, ..., k, holds xij = zj.

  Given two sequences X and Y, a sequence Z is a common subsequence of X and Y if Z is 
  a subsequence of both X and Y . 

  The longest-common-subsequence problem. Given two sequences X = <x1, x2, ..., xm> 
  and Y = <y1, y2, ..., yn>, find a maximum length common subsequence of X and Y.
  """
  m = len(X)
  n = len(Y)
  c = [[0 for j in range(n + 1)] for i in range(m + 1)]

  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if X[i - 1] == Y[j - 1]:
        c[i][j] = c[i - 1][j - 1] + 1
      elif c[i - 1][j] >= c[i][j - 1]:
        c[i][j] = c[i - 1][j]
      else:
        c[i][j] = c[i][j - 1]

  return construct(X, Y, c)

def lcs_memoized(X, Y):
  """
  An O(m*n) memoized approach to the LCS problem
  """
  m = len(X)
  n = len(Y)
  ui = -1
  c = [[ui for j in range(n + 1)] for i in range(m + 1)]

  def lcs_memoized_impl(i, j):
    if i == 0 or j == 0:
      return 0

    if c[i][j] != ui:
      return c[i][j]

    if X[i - 1] == Y[j - 1]:
      c[i][j] = lcs_memoized_impl(i - 1, j - 1) + 1
    else:
      c[i][j] = max(lcs_memoized_impl(i, j - 1),
                    lcs_memoized_impl(i - 1, j))
    return c[i][j]

  lcs_memoized_impl(m, n)
  return construct(X, Y, c)

def lcs_cheap(X, Y):
  """
  Computes the length of an LCS using only min(m, n) entries in the c table
  plus O(1) additional space
  """
  return 0

class Tests(unittest.TestCase):
  def test_motivational_dna(self):
    self.assertEqual(lcs(list('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'),
                         list('GTCGTTCGGAATGCCGTTGCTCTGTAAA')),
                         list('GTCGTCGGAAGCCGGCCGAA'))

  def test_motivational_dna_memoized(self):
    self.assertEqual(lcs_memoized(list('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA'),
                                  list('GTCGTTCGGAATGCCGTTGCTCTGTAAA')),
                                  list('GTCGTCGGAAGCCGGCCGAA'))

  def test_motivational_dna_cheap(self):
    X = list('ACCGGTCGAGTGCGCGGAAGCCGGCCGAA')
    Y = list('GTCGTTCGGAATGCCGTTGCTCTGTAAA')
    self.assertEqual(len(lcs(X, Y)), lcs_cheap(X, Y))

  def test_motivational_lcs_example(self):
    self.assertEqual(lcs(list('ABCBDAB'), list('BDCABA')), list('BCBA'))

  def test_motivational_lcs_example_memoized(self):
    self.assertEqual(lcs_memoized(list('ABCBDAB'), list('BDCABA')),
                     list('BCBA'))

  def test_motivational_lcs_example(self):
    X = list('ABCBDAB')
    Y = list('BDCABA')
    self.assertEqual(len(lcs(X, Y)), lcs_cheap(X, Y))
  
  def test_indexing(self):
    self.assertEqual(lcs(list('ABC'), list('AC')), list('AC'))

  def test_indexing_memoized(self):
    self.assertEqual(lcs_memoized(list('ABC'), list('AC')), list('AC'))

  def test_indexing_cheap(self):
    X = list('ABC')
    Y = list('AC')
    self.assertEqual(len(lcs(X, Y)), lcs_cheap(X, Y))

  def test_15_4_1(self):
    self.assertEqual(lcs(list('10010101'), list('010110110')), list('100110'))

  def test_15_4_1_memoized(self):
    self.assertEqual(lcs_memoized(list('10010101'), list('010110110')),
                                  list('100110'))

  def test_15_4_1(self):
    X = list('10010101')
    Y = list('010110110')
    self.assertEqual(len(lcs(X, Y)), lcs_cheap(X, Y))

if __name__ == '__main__':
  unittest.main()