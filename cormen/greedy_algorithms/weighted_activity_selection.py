"""
Consider a modification to the activity-selection problem in which each activity ai
has, in addition to a start and finish time, a value i. The objective is to maximize
the total value of the activities scheduled.
"""
import unittest
import activity_selection_utils as utils

def _areCompatible(S, prior, following):
  """
  Implementation companion of select_recursively
  """
  utils.check_activities_ordering([S[p] for p in prior])
  utils.check_activities_ordering([S[f] for f in following])
  if not prior:
    return True
  if not following:
    return True

  return S[prior[-1]][1] <= S[following[0]][0]

def _getTotalWeight(S, A):
  """
  Implementation companion of select_recursively
  """
  return sum([S[a][2] for a in A])

def _select_recursively(S, b, e):
  """
  Implementation companion of select_recursively
  """
  # There is nothing to select
  if b == e:
    return []

  # Only option
  if b + 1 == e:
    return [b]

  A = []
  # Pick minimum weight among available activities
  Aweight = min([a[2] for a in S[b:e]])

  for i in range(b, e):
    # Find optima for prior activities
    prior = _select_recursively(S, b, i)
    if not _areCompatible(S, prior, [i]):
      prior = []

    # Find optima for following activities
    following = _select_recursively(S, i+1, e)
    if not _areCompatible(S, [i], following):
      following = []

    # Update global optima
    candidate = prior + [i] + following
    candidateWeight = _getTotalWeight(S, candidate)
    if Aweight <= candidateWeight:
      A = candidate
      Aweight = candidateWeight

  return A

def select_recursively(S):
  """
  Computes a subset of compatible activities so that their total weight is maximal

  Parameters
  ----------
  S : list of (int, int, int)
    A list of ordered by finish time activities: (start time, finish time, weight)

  Returns
  -------
  list of int
    Indexes of input activities that form an optimal solution
  """
  utils.check_activity_selfconsistency(S)
  utils.check_activities_ordering(S)
  return _select_recursively(S, 0, len(S))

def _get_index(b, e, n):
  """
  Implementation companion of select_bottom_up
  """
  i = int((2 * n + -1 * (b - 1)) / 2 * b) + e
  return i

def _get_subproblem_optima(As, b, e, n):
  """
  Implementation companion of select_bottom_up
  """
  i = _get_index(b, e, n)
  return As[i]

def _set_subproblem_optima(As, b, e, n, optima):
  """
  Implementation companion of select_bottom_up
  """
  i = _get_index(b, e, n)
  As[i] = optima
  
def select_bottom_up(S):
  """
  Computes a subset of compatible activities so that their total weight is maximal

  Parameters
  ----------
  S : list of (int, int, int)
    A list of activities ordered by finish time: (start time, finish time, weight)

  Returns
  -------
  list of int
    Indexes of input activities that form an optimal solution
  """
  n = len(S)
  # Sacrificing memory to allow fast compatibility checks 
  As = [[]] * int((n + 1) * (n + 2) / 2)

  for k in range(n+1):
    for b in range(n+1-k):
      e = b + k
      Aweight = 0
      for i in range(b, e):
        # Pick optima for prior activities
        prior = _get_subproblem_optima(As, b, i, e)
        if not _areCompatible(S, prior, [i]):
          prior = []

        # Pick optima for following activities
        following = _get_subproblem_optima(As, i+1, e, n)
        if not _areCompatible(S, [i], following):
          following = []

        # Update local optima to reuse at upcoming steps
        candidate = prior + [i] + following
        candidateWeight = _getTotalWeight(S, candidate)
        if Aweight <= candidateWeight:
          _set_subproblem_optima(As, b, e, n, candidate)
          Aweight = candidateWeight
        
  # Unveil the global optima
  return _get_subproblem_optima(As, 0, n, n)

class Tests(unittest.TestCase):
  def setUp(self):
    self.simplestS = [(0, 2, 1), (1, 4, 4), (3, 5, 2)]
    self.simplestA = [[1]]

    self.motivationalS = [(0, 2, 1), (1, 4, 2), (3, 6, 1), (5, 8, 2), (7, 9, 1)]
    self.motivationalA = [[1, 3]]

    self.parallelS = [(0, 2, 1), (1, 4, 4), (3, 6, 2), (1, 7, 11), (5, 8, 5), (7, 9, 3)]
    self.parallelA = [[3, 5]]

    self.equalS = [(1, 4, 1), (3, 5, 1), (0, 6, 1), (5, 7, 1), (3, 9, 1), (5, 9, 1),
                   (6, 10, 1), (8, 11, 1), (8, 12, 1), (2, 14, 1), (12, 16, 1)]
    self.equalA = [[0, 3, 7, 10], [1, 3, 8, 10]]

  def test_select_recursively_simplest(self):
    self.assertIn(select_recursively(self.simplestS), self.simplestA)

  def test_select_bottom_up_simplest(self):
    self.assertIn(select_bottom_up(self.simplestS), self.simplestA)

  def test_select_recursively_motivational(self):
    self.assertIn(select_recursively(self.motivationalS), self.motivationalA)

  def test_select_bottom_up_motivational(self):
    self.assertIn(select_bottom_up(self.motivationalS), self.motivationalA)

  def test_select_recursively_parallel(self):
    self.assertIn(select_recursively(self.parallelS), self.parallelA)

  def test_select_bottom_up_parallel(self):
    self.assertIn(select_bottom_up(self.parallelS), self.parallelA)

  def test_select_recursively_equal(self):
    self.assertIn(select_recursively(self.equalS), self.equalA)

  def test_select_bottom_up_equal(self):
    self.assertIn(select_bottom_up(self.equalS), self.equalA)
    
if __name__ == '__main__':
  unittest.main()