import numpy as np

def power_step(a, v, zero_cols, alpha=0.15):
    """Performs one step of the power method

    Parameters:

    a: 2D sparce SciPy matrix
    v: 1D NumPy array
    zero_cols: 1D NumPy array
    alpha: float for the damping factor

    Returns:

    The result of performing one step of the power method, including
    reflecting boundaries and damping

    Roughly speaking, it should return the vector

    (1 - alpha)(av + (1/n)w) + (alpha/n)u

    where w and u are vectors which represent boundary reflection and
    damping, respectively

    Notes:

    zero_col has the property that zero_col[i] == 1 if column i of 'a'
    is all zeros, and zero_col[i] == 0 otherwise.

    """
    n = len(v)

    # boundry reflection
    boundry_reflector = zero_cols.dot(v)

    # damping
    damping_vector = np.ones(n) * np.sum(v)

    av = a.dot(v)
    result = (1 - alpha) * (av + ((1/n) * boundry_reflector)) + ((alpha/n) * damping_vector)

    return result

def print_error_log(num_iter, s):
    print(f'    | error after {num_iter} iterations: {s}')

def l1_error(u, v):
    """Computes the L1 error of two vectors

    Parameters:

    u: 1D NumPy array
    v: 1D NumPy array

    Returns:

    The sum of the absolute values of the differences of the entries
    of u and v

    """
    return np.sum(np.abs(u - v))

def power_iter(a, start, zero_cols, tol=0.001, alpha=0.15):
    """Computes a steady state via the power method

    Parameters:
    a: 2D sparse SciPy matrix
    start: 1D NumPy matrix, starting point for the power method
    zero_cols: 1D NumPy array (see docstring for power_step)
    tol: float for error tolerance
    alpha: float for the damping factor

    Returns:
    The result of repeated applications of power_step until the
    l1_error between consecutive vectors is below the given error
    tolerance

    Notes:
    It should call print_error_log every 10 iterations, and one last
    time for the last iteration
    """
    num_iter = 0
    v = start.copy() 
    l1_err = tol + 1  

    while l1_err > tol:
        v_prime = power_step(a, v, zero_cols, alpha)
        l1_err = l1_error(v, v_prime)
        v = v_prime

        num_iter += 1
        if num_iter % 10 == 0 or l1_err <= tol:
            print_error_log(num_iter, l1_err)

    return v_prime


top_five_stanford = [281, 67, 1352, 4898, 3367] # TODO: Fill this in
top_five_berkstan = [288238, 9, 225465, 54130, 1283] # TODO: Fill this in
top_five_google = [115,2138,2560,3178,1950] # TODO: Fill this in
