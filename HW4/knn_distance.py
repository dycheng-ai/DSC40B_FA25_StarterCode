import random

def knn_distance(arr, q, k):
    """Compute the kth nearest point and the distance to it."""
    #just apply quickselect

    diffs = [abs(x-q) for x in arr]

    def quickselect(indices, k):
        if len(indices) == 1:
            return indices[0]

        pivot_index = random.choice(indices)
        pivot_value = diffs[pivot_index]

        lows = [i for i in indices if diffs[i] < pivot_value]
        highs = [i for i in indices if diffs[i] > pivot_value]
        pivots = [i for i in indices if diffs[i] == pivot_value]

        if k <= len(lows):
            return quickselect(lows, k)
        elif k <= len(lows) + len(pivots):
            return pivots[0]
        else: 
            return quickselect(highs, k-len(lows)-len(pivots))
    
    indices = list(range(len(arr)))
    kth_index = quickselect(indices, k)
    return (diffs[kth_index], arr[kth_index])

