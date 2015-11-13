def recursive(p, n):
  if n <= 0:
    return 0

  q = p[n-1]
  for i in range(1, n):
    q = max(q, p[i-1] + recursive(p, n-i))

  return q

def top_down(p, n):
  r = [None for i in range(n)]
  return top_down_imp(p, n, r)

def top_down_imp(p, n, r):
  if n <= 0:
    return 0

  if r[n-1] is not None:
    return r[n-1]

  r[n-1] = p[n-1]
  for i in range(1, n):
    r[n-1] = max(r[n-1], p[i-1] + top_down_imp(p, n-i, r))

  return r[n-1]

def bottom_up(prices, total_length):
  if total_length <= 0:
    return 0

  optimals = [None for i in range(total_length)]
  dirty_cuts = [None for i in range(total_length)]
  for i in range(0, total_length):
    optimals[i] = prices[i]
    dirty_cuts[i] = i
    for j in range(0, i):
      test = prices[j] + optimals[i-j-1]
      if optimals[i] < test:
        optimals[i] = test
        dirty_cuts[i] = j
  
  i = total_length
  cuts = []
  while i > 0:
    cuts.append(dirty_cuts[i-1] + 1)
    i = i - dirty_cuts[i-1] - 1

  return (optimals[n-1], cuts)

# Test 1
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print("\nPrices are", p)
for n in range(1, len(p) + 1):
  print("Optimal solution for n =", n, "is",
        recursive(p, n), top_down(p, n), bottom_up(p, n))

# Test 2
p = [1, 1, 100, 1, 1, 1, 1, 1, 1, 1]
print("\nPrices are", p)
for n in range(1, len(p) + 1):
  print("Optimal solution for n =", n, "is",
        recursive(p, n), top_down(p, n), bottom_up(p, n))
