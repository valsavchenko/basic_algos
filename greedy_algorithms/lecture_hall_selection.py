"""
Given a set of activities to schedule among a large number of lecture halls,
where any activity can take place in any lecture hall. Schedule all the
activities using as few lecture halls as possible
"""
import unittest
import datetime

def assign_halls(activities, halls):
  class Activity:
    # A node for conflicts graph
    def __init__(self):
      self.hall = None # Name of hall 
      self.competitors = [] # References to conflicting activities

    def add(self, competitor):
      assert competitor is not self
      self.competitors.append(competitor)

    def hasHall(self):
      return self.hall is not None
  
    def assign(self, hall):
      assert self.hall is None
      self.hall = hall

  # Create conflicts graph in O(NN)
  conflicts = {act: Activity() for act in activities}
  for act in sorted(activities):
    # Assume that it takes O(1) to retrieve time given activity name
    time = activities[act]
    for a in sorted(activities):
      if a == act:
        # Do not check activity against itself
        continue
      t = activities[a]
      early, late = (time, t) if time[0] < t[0] else (t, time)

      if early[0] < early[1] < late[0] < late[1]:
        # Activities are not in conflict and do not cross midnight
        continue
      elif late[1] < early[0] < early[1] < late[0]:
        # Activities are not in conflict and one of them crosses midnight
        continue
      
      conflicts[act].add(conflicts[a])
        
  # Invest, presumably O(NlogN), into sorting to make the routine "stable"
  root = conflicts[sorted(conflicts)[0]]
  root.hall = 0
  # Assign halls to activities
  while root:
    # Maintain an O(1) lookup vector to quickly check whether hall occupied or not 
    hlls = [False for i in halls]
    hlls[root.hall] = True
    # Exclude halls that could not be used due to restrictions of the problem
    for comp in root.competitors:
      # Exclude hall taken by a competitor
      if comp.hasHall():
        hlls[comp.hall] = True

      # Exclude halls taken by competitors of the competitor as well
      for c in comp.competitors:
        if c.hasHall():
          hlls[c.hall] = True

    # Assign halls for competitors
    hall = 0
    rt = None
    for comp in root.competitors:
      # Skip activities that already have halls
      if comp.hasHall():
        continue
      # Find next available hall
      while hlls[hall]:
        # FIXME: What will happen if there are too few halls?
        hall += 1
      comp.hall = hall
      hlls[hall] = True
      # Consider last assigned activity as a new root
      rt = comp
    root = rt

  return {act: conflicts[act].hall for act in conflicts}

class Tests(unittest.TestCase):
  def test_crown_graph_6(self):
    acts = {'math': (datetime.time(9), datetime.time(12)),
            'pe': (datetime.time(11), datetime.time(14)),
            'phys': (datetime.time(13), datetime.time(16)),
            'dance': (datetime.time(15), datetime.time(18)),
            'draw': (datetime.time(17), datetime.time(20)),
            'sleep': (datetime.time(19), datetime.time(10))}
    halls = [i for i in range(len(acts))]

    golden = {'dance': 0,
              'phys': 2,
              'draw': 1,
              'pe': 3,
              'math': 1,
              'sleep': 0}

    self.assertEqual(assign_halls(acts, halls), golden)

if __name__ == '__main__':
  unittest.main()