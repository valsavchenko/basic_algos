import unittest

def select(S):
  return []

class ActivitySelection(unittest.TestCase):
  def test_motivational(self):
    S = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9),
         (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    self.assertEqual(select(S), [0, 3, 7, 10])
    
if __name__ == '__main__':
  unittest.main()