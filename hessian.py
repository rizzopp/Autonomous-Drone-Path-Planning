import numpy as np
n_poly = 5
n_wps = 4
n_derivative = 4
v_time = np.linspace(0, 5, 6) #5 sec step 1


#a_constraints = np.empty((n_poly+1, n_wps))
#a_constraints[:] = np.nan

for way_point in range(0, n_wps):
    H_row = np.zeros(n_poly+1)
    t0 = v_time[way_point]
    tend = v_time[way_point+1]

    for i in range(0, n_poly):
        for l in range(0, n_poly):
            if i >= n_derivative and l >= n_derivative:
                