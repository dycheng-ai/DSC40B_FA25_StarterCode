import dsc40graph

def biggest_descendent(graph, root, value, biggest=None):
    '''
    Finds the biggest descendent of each node in a tree.
    '''
    result = {}

    def dfs(node):
        max_val = value[node]
        for child in graph.neighbors(node):
            child_max = dfs(child)
            if child_max > max_val:
                max_val = child_max
        result[node] = max_val
        return max_val

    dfs(root)
    return result
