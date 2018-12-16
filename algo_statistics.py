from localsearch import *
from CSP import *
from course_setup import *
from weighted_courses import *
from have_to_take import *


# GROUP ONE
# 0. on the graph, title needs to include that this is for non-honor track
# 1. run each of the following three () a bunch of iterations (1000? 10000?), then compare speed of each
# 2. out of those iterations, for each funtion, draw the histogram of the most frequent courses
iterative_less_conflicts()
simulated_annealing()
backtracking(CSP_initial)

# GROUP TWO
# 0. on the graph, title needs to include that this is for non-honor track
# 0.5 title includes that in this example, the must-takes are: 182, 124, 61
# 1. run each of the following three () a bunch of iterations (1000? 10000?), then compare speed of each
# 2. out of those iterations, for each funtion, draw the histogram of the most frequent courses
iterative_less_conflicts_have_to_take()
backtracking(set_CSP_initial())

# GROUP THREE
# 1. run a bunch of iterations (1000? 10000?), then calculate speed
# 2. simulated_annealing_weighted()[1] is the utility, calculate the expected utility out of those iterations
simulated_annealing_weighted()
