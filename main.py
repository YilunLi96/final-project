from localsearch import *
from CSP import *

# print sort_class(iterative_less_conflicts())

# print sort_class(simulated_annealing())

CSP_initial = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print backtracking(CSP_initial)

# print courses['Stat110']

# print len(course_catalog)

# print countViolations('CS182', ['Math21a', 'Math21b', 'CS50', 'CS161', 'CS121', 'CS124', 'CS61', 'CS134', 'CS136', 'CS181'])

# print countViolations('Math21a', ['Math21a', 'Math21b', 'CS50', 'CS161', 'CS121', 'CS124', 'CS61', 'CS134', 'CS136', 'CS181'])
# print distribute_courses_to_req(['Math21a', 'Math21b', 'CS50', 'CS161', 'CS121', 'CS124', 'CS61', 'CS134', 'CS136', 'CS181'])

# print count_courselist_totalviolations(['Math21a', 'Math21b', 'CS50', 'CS161', 'CS121', 'CS124', 'CS61', 'CS134', 'CS136', 'CS181'])
