from readdata import *
from course_setup import *
import random


def count_courselist_totalviolations(list_of_courses):
	violations = 0
	vio_list = []
	for course in list_of_courses:
		v = countViolations(course, list_of_courses)
		violations += v
		vio_list.append(v)
	return (violations, vio_list)


def hill_climbing():
	course_lst = random.sample(list(courses), 10)

	while count_courselist_totalviolations(course_lst)[0] != 0:
		# delete biggest violation course from course_lst
		# loop through courses not in course_lst such that adding it doesn't add violation or violation decreases
		# add first one found
		# next iteration of while loop

	return course_lst

print hill_climbing()

# print len(course_catalog)