"""
Collection of functions used for digraphs,
plus some example digraphs.
"""
EX_GRAPH0 = {
    0: set([1, 2]),
    1: set([]),
    2: set([])
}

EX_GRAPH1 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3]),
    3: set([0]),
    4: set([1]),
    5: set([2]),
    6: set([])
}

EX_GRAPH2 = {
    0: set([1, 4, 5]),
    1: set([2, 6]),
    2: set([3, 7]),
    3: set([7]),
    4: set([1]),
    5: set([2]),
    6: set([]),
    7: set([3]),
    8: set([1, 2]),
    9: set([0, 4, 5, 6, 7, 3])
}

def make_complete_graph(num_nodes):
    """
    Return a dict representing a graph of size
    num_nodes with all nodes fully connected to
    all other nodes.
    """
    digraph = {}
    for curr_node in range(num_nodes):
        out_node_list = []
        # Add all nodes which are not the current node
        # to the adjacency list for the current node
        for node in range(num_nodes):
            if node != curr_node:
                out_node_list.append(node)
        digraph[curr_node] = set(out_node_list)             
    
    return digraph

def compute_in_degrees(digraph):
    """
    Return a dict containing the in-degrees
    of each node in the digraph.
    """
    in_degrees = {}
    
    # Init value for each node in the dict to 0
    for node in digraph.keys():
        in_degrees[node] = 0
        
    # Compute in-degrees for each node
    for node, out_nodes in digraph.items():
        for out_node in out_nodes:
            in_degrees[out_node] += 1

    return in_degrees        

def in_degree_distribution(digraph):
    """
    Return a dict containing the non-normalized
    distribution of in-degrees given all the
    nodes in the digraph.
    """
    in_degrees_dist = {}
    
    # Obtain a dict of the in degrees for each node
    # in the digraph
    in_degrees = compute_in_degrees(digraph)
    
    # Initialize the in_degrees_dist dict to have
    # keys corresponding to the in-degrees of nodes
    # from the input digraph, and set the values
    # mapped to those keys to zero
    for item in set(in_degrees.values()):
        in_degrees_dist[item] = 0
    
    # Count the number of nodes with a particular in degree
    for in_degree in in_degrees.values():
        in_degrees_dist[in_degree] += 1
            
    return in_degrees_dist