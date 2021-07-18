# A function to compute i-th Fibonacci number (the sum of the two previous ones):
# F0 = 0
# F1 = 1
# Fi = Fi-1 + Fi-2
# in O(n)-time dynamic programming algorithm
def ith_fibonacci(i):
  if i == 0:
    return 0
  if i == 1:
    return 1

  im1 = 1
  im2 = 0
  ith = 0
  while 2 <= i:
    ith = im1 + im2
    im2 = im1
    im1 = ith
    i = i - 1

  return ith

# Test 1
for i in range(11):
  print(i, "-th Fibonacci number is ", ith_fibonacci(i), sep = '')

# Test 2
assert(ith_fibonacci(130) == 659034621587630041982498215)
assert(ith_fibonacci(428) == 125090700579089545268174422433569433531336921195894847055310250098200676237081739043824861)