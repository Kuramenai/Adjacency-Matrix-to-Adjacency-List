import unittest

from reachable_nodes_in_graph import reachable

class TestFindReachableNodesInGraph(unittest.TestCase):
    def test_find_reachable_nodes_1(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        expected_result = {0, 1, 2, 3, 4}
        self.assertEqual(reachable(adj_list, 0), expected_result)

    def test_find_reachable_nodes_2(self):
        adj_list = [[1, 3], [2], [0], [4], [3], []]
        expected_result = {3, 4}
        self.assertEqual(reachable(adj_list, 3), expected_result)
    
    def test_find_reachable_nodes_3(self):
        adj_list = [[]]
        expected_result = {0}
        self.assertEqual(reachable(adj_list, 0), expected_result)
    
    def test_find_reachable_nodes_4(self):
        adj_list = [[]]
        expected_result = None
        self.assertEqual(reachable(adj_list, 1), expected_result)
    
    def test_find_reachable_nodes_5(self):
        adj_list = [[1]]
        expected_result = None
        self.assertEqual(reachable(adj_list, 0), expected_result)
    

if __name__ == "__main__":
  unittest.main()