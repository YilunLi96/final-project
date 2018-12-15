from localsearch import *
from CSP import *
from course_setup import *
from weighted_courses import *


print sort_class(iterative_less_conflicts())

print sort_class(simulated_annealing())

print backtracking(CSP_initial)
