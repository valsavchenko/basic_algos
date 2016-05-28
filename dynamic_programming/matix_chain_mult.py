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
  m = [reduce(mul, p)] * int(n * (n-1) / 2)
  s = [0] * len(m)
  
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
  optimal = [queue[0][1]]
  while queue:
    top = queue.pop(0)

    if top[0] == top[1]:
      optimal.insert(0, top[0])
      continue

    q0 = (top[0], s[ind(top[0], n, top[1])])
    if q0[0] == q0[1]:
      optimal.insert(0, q0[0])
    else:
      queue.insert(0, q0)

    q1 = (q0[1]+1, top[1])
    if q1[0] == q1[1]:
      if not optimal or optimal[0] != q0[0]:
        optimal.insert(0, q1[0])
    else:
      queue.insert(0, q1)

  return m[ind(0, n, n-1)]   

class Tests(unittest.TestCase):
  def test_motivational(self):
    self.assertEqual(matrix_chain_mult((10, 100, 5, 50)), 7500)

  def test_step3(self):
    self.assertEqual(matrix_chain_mult((30, 35, 15, 5, 10, 20, 25)), 15125)

if __name__ == '__main__':
  unittest.main()