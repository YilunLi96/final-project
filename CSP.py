from readdata import *
from course_setup import *
import random
import math


# 0, make a copy of the course catalog
catalog = read_catalog()

# 1, Order the requirements to be satisfied (Variable Ordering)
reqs = ['linalg', 'calc', 'basic', 'basic', 'boaz', 'theory', 'tech', 'tech', 'breadth', 'breadth']


def backtracking():
	return recursive_backtracking()

def recursive_backtracking(assignment):
	if course_list_complete(assignment):
		return assignment

	else:
		class_index = next_class_to_fill(assignment)
		requirement_to_fill = reqs[class_index]
	return assignment


# allowing duplicates returns list of classes that satisfy the requirement located at class_id
def valid_options(class_id):


# returns true if there are no violations from duplicates or prereqs, otherwise false
# no need to check from requirements since we know the order they are satisfied in
def no_violations(c_list):

# returns a list of all valid successor course lists
def get_all_successors(c_list):
    # call next_class_to_fill to get next class_id

    # call valid_options for a list of classes that satisfy the next req

    # create empty list to hold course lists that will be returned
    # for each class in this list
        # if inserting this class causes no conflicts append updated course list to list of successors
        # use no_violations to do this

    # return list of successor course lists

###### SOLVE CSP FROM SUDOKU ######
def solveCSP(problem):
    statesExplored = 0
    # problem is the list of courses start with course list all zeroes
    frontier = [problem]
    while frontier:
        state = frontier.pop()

        statesExplored += 1
        # once list completely assigned we are done, possible error checking is done
        if course_list_complete(state):
            print 'Number of explored: ' + str(statesExplored)
            return state
        else:
            successors = state.getAllSuccessors()
            frontier.extend(successors)

    return None

initial_courses = [0,0,0,0,0,0,0,0,0,0]
print solveCSP(initial_courses)