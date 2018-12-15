from readdata import *
from course_setup import *
import random
import math


def backtracking():
	return recursive_backtracking()

def recursive_backtracking(assignment):
	if course_list_complete(assignment):
		return assignment

	else:
		class_index = next_class_to_fill(assignment)
		possible_courses = valid_options(class_index)
		
	return None


# # returns true if there are no violations from duplicates or prereqs, otherwise false
# # no need to check from requirements since we know the order they are satisfied in
# def no_violations(c_list):

# # returns a list of all valid successor course lists
# def get_all_successors(c_list):
#     # call next_class_to_fill to get next class_id

#     # call valid_options for a list of classes that satisfy the next req

#     # create empty list to hold course lists that will be returned
#     # for each class in this list
#         # if inserting this class causes no conflicts append updated course list to list of successors
#         # use no_violations to do this

#     # return list of successor course lists
