import unittest

from adjacency_matrix_to_adjacency_list import mat_to_list

class TestConversionMatList(unittest.TestCase):
    def test_conversion_correct_1(self):
        adj_mat =  [[0, 1, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0],
                    [0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0]]
        
        expected_result = [[1, 3], [2], [0], [4], [3], []]
        self.assertEqual(mat_to_list(adj_mat), expected_result)
      
    def test_conversion_correct_2(self):
        adj_mat = [ [0, 0, 1], 
                    [0, 0, 1], 
                    [1, 1, 0]]
        
        expected_result = [[2], [2], [0, 1]]
        self.assertEqual(mat_to_list(adj_mat), expected_result)
    
    def test_conversion_correct_3(self):
        adj_mat = []
        expected_result = []
        self.assertEqual(mat_to_list(adj_mat), expected_result)

    def test_conversion_correct_4(self):
        adj_mat = [1, 2, 3]
        expected_result = None
        self.assertEqual(mat_to_list(adj_mat), expected_result)    

    def test_conversion_correct_5(self):
        adj_mat = [[0, 1, 0], [1, 0, 0], 1]
        expected_result = None
        self.assertEqual(mat_to_list(adj_mat), expected_result)    

    
if __name__ == "__main__":
  unittest.main()