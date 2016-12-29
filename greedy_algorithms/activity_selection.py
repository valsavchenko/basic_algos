"""
S - set of activities. I-th element of it corresponds to ai activity and
is represented as a pair (si, fi), where si is start time and fi is end time,
it is assumed that 0 <= si < fi < Inf. It's assumed that activities are sorted
in monotonically increasing order of finish time.

Activities ai and aj are compatible if si >= fj or sj >= fi

In the activity selection problem the goal is to select a maximum-size subset
of mutually compatible activities.
"""

import unittest

def min_finish_greedy_selector(S):
  """
  Implements an O(len(S)) greedy approach to the problem
  """
  assert all(0 <= S[i][0] and S[i][0] < S[i][1] and S[i][1] < float('Inf') for i in range(len(S)-1)),\
    'Start times are assumed to be creater than 0 and less then finish times'
  assert all(S[i][1] <= S[i+1][1] for i in range(len(S)-1)),\
    'Activities are assumed to be ordered by finish time'
  A = [0]
  for i in range(1, len(S)):
    currentActivity = A[-1]
    currentFinishTime = S[currentActivity][1]
    nextStartTime = S[i][0]
    if currentFinishTime <= nextStartTime:
      A.append(i)
  return A

class ActivitySelection(unittest.TestCase):
  def test_motivational(self):
    S = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9),
         (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    self.assertEqual(min_finish_greedy_selector(S), [0, 3, 7, 10])
    
if __name__ == '__main__':
  unittest.main()