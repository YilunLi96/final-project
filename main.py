from localsearch import *
from CSP import *
from course_setup import *
from weighted_courses import *
from have_to_take import *


# 1
print iterative_less_conflicts()

# 2
print simulated_annealing()

# 3
print backtracking(CSP_initial)

# 4
print backtracking(set_CSP_initial())

# 5
print iterative_less_conflicts_have_to_take()

# 6
print simulated_annealing_weighted()

# 7
print CSP_uniform_cost_weighted(CSP_initial2)
