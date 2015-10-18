def recursive(p, n):
  if n == 0:
    return 0
  q = p[n-1]
  for i in range(1, n):
    q = max(q, p[i-1] + recursive(p, n-i))
  return q

def top_down(p, n):
  r = [None for i in range(n)]
  return top_down_imp(p, n, r)

def top_down_imp(p, n, r):
  if n == 0:
    return 0
  if r[n-1] is not None:
    return r[n-1]
  r[n-1] = p[n-1]
  for i in range(1, n):
    r[n-1] = max(r[n-1], p[i-1] + top_down_imp(p, n-i, r))
  return r[n-1]

def bottom_up(p, n):
  pass 

# Test 1
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print("Prices are", p)
for n in range(1, 11):
  print("Optimal solution for n =", n,  "is",
        recursive(p, n), top_down(p, n), bottom_up(p, n))
