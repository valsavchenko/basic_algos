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

def costly_cuts(prices, cut_price, total_length):
  assert total_length <= len(prices), "Not enough prices to find an optimal solution"
  assert 0 <= cut_price, "Cut price is assumed to be positive"

  optimals = [None for i in range(total_length)]
  dirty_cuts = [None for i in range(total_length)]
  for i in range(0, total_length):
    optimals[i] = prices[i]
    dirty_cuts[i] = i
    for j in range(0, i):
      test = prices[j] - cut_price + optimals[i-j-1]
      if optimals[i] < test:
        optimals[i] = test
        dirty_cuts[i] = j
  
  i = total_length
  cuts = []
  while i > 0:
    cuts.append(dirty_cuts[i-1] + 1)
    i = i - dirty_cuts[i-1] - 1

  return (optimals[total_length-1], cuts)

def bottom_up(prices, total_length):
  return costly_cuts(prices, 0, total_length)

def max_density(prices, total_length):
  density = [prices[i] / (i + 1) for i in range(total_length)]

  best_price = 0
  cuts = []
  while total_length > 0:
    actual_density = density[:total_length]
    opt = max(actual_density)
    i = actual_density.index(opt) 
    total_length = total_length - i - 1
    best_price = best_price + prices[i]
    cuts.append(i + 1)

  return (best_price, cuts)

def test(p, c):
  print("\np = ", p, "c =", c)
  for n in range(1, len(p) + 1):
    print("Optimal solution for n =", n, "is\n\t",
          "recursive =", recursive(p, n),
          "top_down =", top_down(p, n),
          "bottom_up =", bottom_up(p, n),
          "max_density =", max_density(p, n),
          "costly_cuts =", costly_cuts(p, c, n))

# Test 1
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
test(p, 2)

# Test 2
p = [1, 1, 100, 1, 1, 1, 1, 1, 1, 1]
test(p, 2)