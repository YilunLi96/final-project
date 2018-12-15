from localsearch import *
from CSP import *
from course_setup import *

CSP_initial = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# # Honor Track
# honor_flag = 0
# #
# honor_flag = 1

# if honor_flag == 0:
# 	CSP_initial = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# else:
# 	CSP_initial = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# if honor_flag == 0:


print sort_class(iterative_less_conflicts())

print sort_class(simulated_annealing())

print backtracking(CSP_initial)
