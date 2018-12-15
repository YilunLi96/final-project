from readdata import *
from course_setup import *
import random
import math

# 0, make a copy of the course catalog

# 1, Order the requirements to be satisfied (Variable Ordering)
reqs = ['linalg', 'calc', 'basic', 'boaz', 'theory', 'tech', 'breadth']

# 2, start filling in courses following that above order
	# 3, search in course catalog courses that satisfies this requirement 
	# 4, randomly choose one course and test if there is violation, if not fill it in; if yes next random course
	# 5, if the requirement is fulfilled, delete all courses that only satisfies this one requirement from course catalog ("filtering")
# 6 repeat until full