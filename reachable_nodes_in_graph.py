import copy

def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node
    

    """
    # TODO
    reachable_nodes = set()

    if adj_list is not None and 0 <= start_node and start_node < len(adj_list):
        adj_list_copy = copy.deepcopy(adj_list)
        stack = [start_node]

        while len(stack) != 0:
            node = stack.pop()

            if node not in reachable_nodes: 
                reachable_nodes.add(node)

                try:
                    for neighbor in adj_list_copy[node]:
                        if neighbor not in reachable_nodes and adj_list_copy[neighbor]:
                            stack.append(neighbor)
                except IndexError:
                    print("Node doesn't exist")
                    return None
            
        return reachable_nodes

    return None

graph = [[1, 3], [2], [0], [4], [3], []]

reachable_nodes = reachable([[]], 4)
print(reachable_nodes)


    

