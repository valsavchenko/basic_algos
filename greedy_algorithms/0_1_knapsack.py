"""
A thief robbing a store finds n items. The i-th item is worth v_i dollars and
weighs w_i pounds, where v_i and w_i are integers. The thief wants to take as
valuable a load as possible, but he can carry at most W pounds in his knapsack,
 for some integer W. Which items should he take?
"""
import unittest

def zero_one_knapsak_problem(vw, W):
  """
  A dynamic-programming solution to the 0-1 knapsack problem that runs in O(nW)
  time, where n is the number of items and W is the maximum weight of items that
  the thief can put in his knapsack.

  Parameters
  ----------
  vw : list of (int, int)
    Value and weight of i-th item

  W : int
    Capacity of a knapsack

  Returns
  -------
  list of int
    Indexes of items to pick for a perfect robbery
  """
  return []

class Tests(unittest.TestCase):
  def setUp(self):
    self.vw162 = [(60, 10), (100, 20), (120, 30)]
    self.W162 = 50
    self.best162 = [[1, 2]]

  def test_16_2(self):
    self.assertIn(zero_one_knapsak_problem(vw = self.vw162, W = self.W162),
                  self.best162)

if __name__ == '__main__':
  unittest.main()