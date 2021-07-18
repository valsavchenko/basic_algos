from operator import mul
from functools import reduce
import unittest

"""
Given a chain <A0, A1, ..., An> of n matrices, where for i = 0, 1, ..., n,
matrix Ai has dimension pi-1 x pi, fully paranthesize the product A0xA1x..xAn
in a way that minimized the number of scalar muliplications.
"""
def matrix_chain_mult(p):
  def ind(i, n, j):
    # Locate element of symmetrical matrix, which is stored in compact form
    # without diagonal elements
    assert(i < j)
    return int(i * (2 * n - i - 3) / 2 + j - 1)

  n = len(p) - 1
  # The minimal number of scalar multiplications needed to compute matrix Ai..j
  m = [reduce(mul, p)] * int(n * (n-1) / 2)
  # Which index of k achieved the optimal cost in computing m[i, j]
  s = [0] * len(m)
  
  for d in range(1, n):
    # Traverse 'diagonals' from the closest to the true diagonal towards the
    # upper right element of the matrix
    for i in range(n-d):
      # Traverse each element on the diagonal
      j = i+d
      ij = ind(i, n, j)

      for k in range(i, j):
        # Find an optimal solution for the sub-problem Ai..j
        m_ik = m[ind(i, n, k)] if i != k else 0
        m_ik1j = m[ind(k+1, n, j)] if k+1 != j else 0        
        m_ij = m_ik + m_ik1j + p[i] * p[k+1] * p[j+1]
        if m_ij < m[ij]:
          m[ij] = m_ij
          s[ij] = k 

  # Queue of sub-problems to analyze and extract optimal positions k
  # in linear fashion
  queue = [(0, n-1)]
  # Sequence of optimal multiplications
  optimal = []
  while queue:
    top = queue.pop(0)

    left = (top[0], s[ind(top[0], n, top[1])])
    optimal.insert(0, left[1])
    if left[0] != left[1]:
      queue.insert(0, left)

    right = (left[1]+1, top[1])
    if right[0] != right[1]:
      pos = 1 if queue[0] == left else 0
      queue.insert(pos, right)

  return (m[ind(0, n, n-1)], optimal)

class Tests(unittest.TestCase):
  def test_motivational(self):
    self.assertEqual(matrix_chain_mult((10, 100, 5, 50)), (7500, [0, 1]))

  def test_step3(self):
    self.assertEqual(matrix_chain_mult((30, 35, 15, 5, 10, 20, 25)), (15125, [3, 4, 1, 0, 2]))

  def test_exercises_15_2_1(self):
    self.assertEqual(matrix_chain_mult((5, 10, 3, 12, 5, 50, 6)), (2010, [4, 2, 3, 0, 1]))

if __name__ == '__main__':
  unittest.main()