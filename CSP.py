from readdata import *
from course_setup import *
import random
import math


def backtracking(assignment):
	return recursive_backtracking(assignment)


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
				assignment[class_index] = course
				result = recursive_backtracking(assignment)
				if result != None:
					return result
				else:
					remove_index = assignment.index(course)
					assignment[remove_index] = 0
		return None
