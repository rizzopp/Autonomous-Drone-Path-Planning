import numpy as np
n_poly = 5
n_wps = 4
n_derivative = 4
v_time = np.linspace(0, 5, 6) #5 sec step 1

""" Constraints matrix """
wp_constraints = np.empty((n_derivative+1, n_wps))
wp_constraints[:] = np.nan

