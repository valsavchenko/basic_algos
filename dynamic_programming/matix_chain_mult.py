from operator import mul
from functools import reduce

"""
A helper to access [i, j]-th element of m stored in compact O(n) array
"""
def ind(i, n, j):
  return int(i * (2 * n - i - 3) / 2 + j - 1)

"""
Given a chain <A1, A2, ..., An> of n matrices, where for i = 1, 2, ..., n,
matrix Ai has dimension pi-1 x pi, fully paranthesize the product A1A2***An
in a way that minimized the number of scalar muliplications.
"""
def matrix_chain_mult(p):
  n = len(p) - 1
  m = [reduce(mul, p)] * n
  
  for d in range(1, n):
    for i in range(n-d):
      j = i+d
      ij = ind(i, n, j)

      for k in range(i, j):
        mik = m[ind(i, n, k)] if i != k else 0
        mik1j = m[ind(k+1, n, j)] if k+1 != j else 0
        m[ij] = min(m[ij], mik + mik1j + p[i] * p[k+1] * p[j+1])

  return m[ind(0, n, n-1)]   

# Test 1 - motivational example
p = (10, 100, 5, 50)
assert(7500 == matrix_chain_mult(p))