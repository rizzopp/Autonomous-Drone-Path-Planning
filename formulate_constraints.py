"""
Path Planning & Optimization for IROS 2018 Competition
DSE Group 25
"""
from input import *

# wps = [1,2]
# n_wps = 4
# n_derivative = 4


def formulate_constraints():
    for way_point in range(0, n_wps):
        for derivative in range(0, n_derivative):
            if not np.isnan(wp_constraints[derivative, way_point]):
                # There is a constraint
                if way_point == 0:
                    '''Starting waypoint -- only initial condition for first poly segment'''
                    pass
                elif way_point == n_wps-1:
                    '''Last waypoint -- only terminal condition for first poly segment'''
                    pass
                else:
                    '''Middle waypoint -- two boundary conditions for every poly segment: initial and terminal'''
                    pass
    pass