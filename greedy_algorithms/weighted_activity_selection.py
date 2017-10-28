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
      continue

    # Find optima for following activities
    following = _select_recursively(S, i+1, e)
    if not _areCompatible(S, [i], following):
      continue

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

class Tests(unittest.TestCase):
  def setUp(self):
    self.motivationalS = [(0, 2, 1), (1, 4, 2), (3, 6, 1), (5, 8, 2), (7, 9, 1)]
    self.motivationalA = [[1, 3]]
  
  def test_recursive_selector(self):
    self.assertIn(select_recursively(self.motivationalS), self.motivationalA)
    
if __name__ == '__main__':
  unittest.main()