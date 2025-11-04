def mode(numbers):
    '''
    Efficiently finds the mode of a list of numbers.
    '''
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1
        else: 
            counts[num] = 1
    
    mode = -999999
    max_val = -999999
    values = list(counts.values())
    keys = list(counts.keys())
    for i in range(len(values)):
        if values[i] > max_val:
            mode = keys[i]
            max_val = values[i]
    
    return mode
