from localsearch import *
from CSP import *
from course_setup import *
from weighted_courses import *
from have_to_take import *


print iterative_less_conflicts()

print simulated_annealing()

print backtracking(CSP_initial)

print simulated_annealing_weighted()

print iterative_less_conflicts_have_to_take()

print backtracking(set_CSP_initial())

print CSP_uniform_cost_weighted(CSP_initial2)