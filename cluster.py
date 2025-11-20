from collections import deque

def cluster(graph, weights, level):
    '''
    Clusters a graph based on similarity.
    '''
    visited = set()
    clusters = []

    for start in graph.nodes:
        if start in visited:
            continue
        component = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            component.add(node)
            for neighbor in graph.neighbors(node):
                if neighbor in visited:
                    continue
                if weights(node, neighbor) < level:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)

        clusters.append(frozenset(component))

    return frozenset(clusters)
