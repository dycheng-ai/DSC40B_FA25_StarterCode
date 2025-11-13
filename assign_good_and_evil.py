from collections import deque

def assign_good_and_evil(graph):
    '''
    Assigns good and evil labels to nodes in a graph.
    '''
    assignment = {}
    visited = set()
    
    nodes = list(graph.nodes)
    
    for start in nodes:
        if start in visited:
            continue
            
        queue = deque([start])
        assignment[start] = 'good'
        visited.add(start)
        
        while queue:
            current = queue.popleft()
            current_color = assignment[current]
            next_color = 'evil' if current_color == 'good' else 'good'
            
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    assignment[neighbor] = next_color
                    queue.append(neighbor)
                elif assignment[neighbor] == current_color:
                    return None
    
    return assignment