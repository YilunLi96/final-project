from readdata import *
from course_setup import *
import random
import math


def backtracking():
	return recursive_backtracking()

def recursive_backtracking(assignment):
	# if assignment is complete return it
	if course_list_complete(assignment):
		return assignment

	else:
		# locate the next class slot to be filled
		class_index = next_class_to_fill(assignment)
		# get all the possible courses that can fulfill the next slot
		possible_courses = valid_options(class_index)

		# go over them
		for course in possible_courses:
			# if it is already in assignment skip it
			if course in assignment:
				continue
			if no_violations(assignment, course):
				assignment = add_course(assignment, course)
				result = recursive_backtracking(assignment)
				if result != None:
					return result
				else:
					assignment = remove_course(c_list, course)

	return None


# returns true if there are no violations from duplicates or prereqs, otherwise false
# no need to check from requirements since we know the order they are satisfied in
def no_violations(c_list, course):
	return True

# replace the first zero in c_list to course
def add_course(c_list, course):
	return c_list

# replace this course with zero
def remove_course(c_list, course):
	return c_list
