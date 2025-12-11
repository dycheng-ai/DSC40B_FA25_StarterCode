def learn_theta(data, colors):
    '''
    Finds theta that is larger than all blue and less than all red.
    '''
    max_blue = float('-inf')
    min_red = float('inf')
    
    for i in range(len(data)):
        if colors[i] == 'blue':
            max_blue = max(max_blue, data[i])
        else:
            min_red = min(min_red, data[i])
    
    return (max_blue + min_red) / 2.0


def compute_ell(data, colors, theta):
    '''
    Computes the loss function L(theta) for a given theta.
    '''
    red_less = 0
    blue_greater = 0
    
    for i in range(len(data)):
        if colors[i] == 'red' and data[i] <= theta:
            red_less += 1
        elif colors[i] == 'blue' and data[i] > theta:
            blue_greater += 1
    
    return float(red_less + blue_greater)



def minimize_ell(data, colors):
    '''
    Finds theta that minimizes the loss function L(theta) using quadratic time complexity.
    '''
    pot_theta = []
    for point in data:
        pot_theta.append(point)
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            midpoint = (data[i] + data[j]) / 2.0
            pot_theta.append(midpoint)
    
    min_loss = float('inf')
    best_theta = None
    
    for theta in pot_theta:
        loss = compute_ell(data, colors, theta)
        if loss < min_loss:
            min_loss = loss
            best_theta = theta
    
    return float(best_theta)


def minimize_ell_sorted(data, colors):
    '''
    Finds theta that minimizes the loss function L(theta) in linear time.
    '''
    candidates = []
    for point in data:
        candidates.append(point)
    
    for i in range(len(data) - 1):
        midpoint = (data[i] + data[i + 1]) / 2.0
        candidates.append(midpoint)
    
    min_loss = float('inf')
    best_theta = None
    
    for theta in candidates:
        loss = compute_ell(data, colors, theta)
        if loss < min_loss:
            min_loss = loss
            best_theta = theta
    
    return float(best_theta)

