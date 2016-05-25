from operator import mul
from functools import reduce
import unittest

"""
Given a chain <A1, A2, ..., An> of n matrices, where for i = 1, 2, ..., n,
matrix Ai has dimension pi-1 x pi, fully paranthesize the product A1A2***An
in a way that minimized the number of scalar muliplications.
"""
def matrix_chain_mult(p):
  def ind(i, n, j):
    return int(i * (2 * n - i - 3) / 2 + j - 1)

  n = len(p) - 1
  nn = int(n * (n-1) / 2)
  m = [reduce(mul, p)] * nn
  s = [0] * nn
  
  for d in range(1, n):
    for i in range(n-d):
      j = i+d
      ij = ind(i, n, j)

      for k in range(i, j):
        m_ik = m[ind(i, n, k)] if i != k else 0
        m_ik1j = m[ind(k+1, n, j)] if k+1 != j else 0        
        m_ij = m_ik + m_ik1j + p[i] * p[k+1] * p[j+1]
        if m_ij < m[ij]:
          m[ij] = m_ij
          s[ij] = k

  queue = [(0, s[ind(0, n, n-1)]), (s[ind(0, n, n-1)]+1, n-1)]
  o = [queue[0][1]]
  while queue:
    q = queue[0]
    queue = queue[1:]

    if q[0] == q[1]:
      o[:0] = [q[0]]
      continue

    q0 = (q[0], s[ind(q[0], n, q[1])])
    if q0[0] == q0[1]:
      o[:0] = [q0[0]]
    else:
      queue[:0] = [q0]

    q1 = (q0[1]+1, q[1])
    if q1[0] == q1[1]:
      if not o or o[0] != q0[0]:
        o[:0] = [q1[0]]
    else:
      queue[:0] = [q1]

  print(o)

  return m[ind(0, n, n-1)]   

class Tests(unittest.TestCase):
  def test_motivational(self):
    self.assertEqual(matrix_chain_mult((10, 100, 5, 50)), 7500)

  def test_step3(self):
    self.assertEqual(matrix_chain_mult((30, 35, 15, 5, 10, 20, 25)), 15125)

if __name__ == '__main__':
  unittest.main()