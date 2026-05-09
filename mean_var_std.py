import numpy as np

def calculate(list):

    if(len(list) != 9):
        raise ValueError('List must contain nine numbers.')
    
    matrix = np.array(list).reshape((3, 3))

    def combine_arrays_to_list(axis1, axis2, flattened):
        return [axis1.tolist(), axis2.tolist(), flattened.item()]

    mean_x = np.mean(matrix, 0)
    mean_y = np.mean(matrix, 1)
    mean_flat = np.mean(matrix)
    mean_list = combine_arrays_to_list(mean_x, mean_y, mean_flat)

    var_x = np.var(matrix, 0)
    var_y = np.var(matrix, 1)
    var_flat = np.var(matrix)
    var_list = combine_arrays_to_list(var_x, var_y, var_flat)

    std_x = np.std(matrix, 0)
    std_y = np.std(matrix, 1)
    std_flat = np.std(matrix)
    std_list = combine_arrays_to_list(std_x, std_y, std_flat)

    max_x = np.max(matrix, 0)
    max_y = np.max(matrix, 1)
    max_flat = np.max(matrix)
    max_list = combine_arrays_to_list(max_x, max_y, max_flat)

    min_x = np.min(matrix, 0)
    min_y = np.min(matrix, 1)
    min_flat = np.min(matrix)
    min_list = combine_arrays_to_list(min_x, min_y, min_flat)

    sum_x = np.sum(matrix, 0)
    sum_y = np.sum(matrix, 1)
    sum_flat = np.sum(matrix)
    sum_list = combine_arrays_to_list(sum_x, sum_y, sum_flat)
    
    calculations = {
        'mean': mean_list,
        'variance': var_list,
        'standard deviation': std_list,
        'max': max_list,
        'min': min_list,
        'sum': sum_list
    }

    return calculations