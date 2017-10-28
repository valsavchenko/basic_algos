"""
Some utilities for variations of activity selection problem
"""

def check_activity_selfconsistency(S):
  concl = all(0 <= S[i][0] and S[i][0] < S[i][1] and S[i][1] < float('Inf')\
              for i in range(len(S)-1))
  assert concl,\
    'Start times are assumed to be greater than 0 and less then finish times'

def check_activities_ordering(S):
  concl = all(S[i][1] <= S[i+1][1] for i in range(len(S)-1))
  assert concl, 'Activities are assumed to be ordered by finish time'