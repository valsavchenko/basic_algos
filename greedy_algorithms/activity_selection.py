"""
S - set of activities. I-th element of it corresponds to a_i activity and
is represented as a pair (s_i, f_i), where s_i is start time and f_i is end time,
it is assumed that 0 <= s_i < f_i < Inf. It's assumed that activities are sorted
in monotonically increasing order of finish time.

Activities a_i and a_j are compatible if f_j <= s_i or f_i <= s_j

In the activity selection problem the goal is to select a maximum-size subset
of mutually compatible activities.
"""

import unittest
import activity_selection_utils as utils

def min_finish_greedy_selector(S):
  """
  Implements an O(len(S)) greedy approach to the problem
  """
  utils.check_activity_selfconsistency(S)
  utils.check_activities_ordering(S)

  A = [0]
  for i in range(1, len(S)):
    currentActivity = A[-1]
    currentFinishTime = S[currentActivity][1]
    nextStartTime = S[i][0]
    if currentFinishTime <= nextStartTime:
      A.append(i)
  return A

def bottom_up_dynamic_selector(S):
  """
  Implements an O(len(S^2)) bottom-up with memoization 
  dynamic programming approach to the problem
  """
  utils.check_activity_selfconsistency(S)
  utils.check_activities_ordering(S)

  def get_index(i, j, n):
    assert i <=  j
    ind = i * n + (1 - i) * i / 2 + (j - i)
    return int(ind)

  n = len(S)
  A = [-1] * int((n + 1) * n / 2)
  c = [0] * len(A)

  for i in range(n):
    for j in range(i+1, n):
      for k in range(i+1, j):
        if not S[i][1] <= S[k][0] or not S[k][1] <= S[j][0]:
          # a_k doesn't belong to S_ij
          continue

        c_ij = c[get_index(i, j, n)]
        c_ik = c[get_index(i, k, n)]
        c_kj = c[get_index(k, j, n)]
        if c_ik + c_kj + 1 < c_ij:
          # Move on if current optima for the S_ij is better
          continue

        A[get_index(i, j, n)] = k
        c[get_index(i, j, n)] = c_ik + c_kj + 1

  AA = []
  q = [(0, n-1)]
  while q:
    i, j = q.pop(0)
    k = A[get_index(i, j, n)]
    if k == -1:
      continue
    AA.append(k)
    q.append((i, k))
    q.append((k, j))
  assert len(AA) == c[get_index(0, n-1, n)]

  AA.append(0)
  if 1 < n and S[0][1] <= S[-1][0]:
    AA.append(n-1)
  AA.sort()

  return AA

class ActivitySelection(unittest.TestCase):
  @classmethod
  def setUpClass(self):
    self.motivationalS = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9),
                          (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    self.motivationalA = [[0, 3, 7, 10],
                          [0, 3, 8, 10]]

    self.singleS = [(4, 10)]
    self.singleA = [0]

    self.pairCompS = [(1, 3), (5, 8)]
    self.pairCompA = [0, 1]

    self.pairNonCompS = [(3, 4), (2, 10)]
    self.pairNonCompA = [0]

    self.threeCompS = [(0, 2), (3, 5), (7, 9)]
    self.threeCompA = [0, 1, 2]

    self.totalOverlapS = [(2, 3), (1, 4), (0, 5)]
    self.totalOverlapA = [[0], [1], [2]]

    self.vS = [(0, 1), (1, 3), (2, 5), (4, 6), (7, 8)]
    self.vA = [0, 1, 3, 4]

  def test_min_finish_greedy_motivational(self):
    self.assertIn(min_finish_greedy_selector(self.motivationalS),
                  self.motivationalA)

  def test_bottom_up_dynamic_selector_motivational(self):
    self.assertIn(bottom_up_dynamic_selector(self.motivationalS),
                  self.motivationalA)

  def test_bottom_up_dynamic_selector_debuggable(self):
    S = [(1, 4), (3, 5), (0, 6), (5, 7)]
    As = [[0, 3], [1, 3]]
    self.assertIn(bottom_up_dynamic_selector(S), As)

  def test_min_finish_greedy_single(self):
    self.assertEqual(min_finish_greedy_selector(self.singleS),
                     self.singleA)

  def test_bottom_up_dynamic_selector_single(self):
    self.assertEqual(bottom_up_dynamic_selector(self.singleS),
                     self.singleA)

  def test_min_finish_greedy_pair_non_comp(self):
    self.assertEqual(min_finish_greedy_selector(self.pairNonCompS),
                     self.pairNonCompA)

  def test_bottom_up_dynamic_selector_pair_non_comp(self):
    self.assertEqual(bottom_up_dynamic_selector(self.pairNonCompS),
                     self.pairNonCompA)

  def test_min_finish_greedy_pair_comp(self):
    self.assertEqual(min_finish_greedy_selector(self.pairCompS),
                     self.pairCompA)

  def test_bottom_up_dynamic_selector_pair_comp(self):
    self.assertEqual(bottom_up_dynamic_selector(self.pairCompS),
                     self.pairCompA)

  def test_min_finish_greedy_three_comp(self):
    self.assertEqual(min_finish_greedy_selector(self.threeCompS),
                     self.threeCompA)

  def test_bottom_up_dynamic_selector_three_comp(self):
    self.assertEqual(bottom_up_dynamic_selector(self.threeCompS),
                     self.threeCompA)

  def test_min_finish_greedy_total_overlap(self):
    self.assertIn(min_finish_greedy_selector(self.totalOverlapS),
                  self.totalOverlapA)

  def test_bottom_up_dynamic_selector_total_overlap(self):
    self.assertIn(bottom_up_dynamic_selector(self.totalOverlapS),
                  self.totalOverlapA)

  def test_min_finish_greedy_v(self):
    self.assertEqual(min_finish_greedy_selector(self.vS),
                     self.vA)

  def test_bottom_up_dynamic_selector_v(self):
    self.assertEqual(bottom_up_dynamic_selector(self.vS),
                     self.vA)
    
if __name__ == '__main__':
  unittest.main()