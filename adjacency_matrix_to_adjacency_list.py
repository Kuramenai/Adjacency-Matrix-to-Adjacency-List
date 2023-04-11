import copy 

def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
    # TODO
    adj_list = []
    if adj_mat is not None:
        adj_mat_copy = copy.deepcopy(adj_mat)
        num_nodes = len(adj_mat_copy)
        neighbors  = []
       
        for node in range(num_nodes):
            try:
                for idx, value in enumerate(adj_mat_copy[node]):
                    if value == 1:
                        neighbors.append(idx)
                adj_list.append(neighbors)
                neighbors = []
            except TypeError:
                print("Input matrix error")
                return None
            
    return adj_list
   

adj_mat =   [[0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0]]

adj_list = mat_to_list([[1, 0, 0], 1])
print(adj_list)