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


# Important: prefers classes with less pre_reqs!
def hill_climbing():
    course_lst = random.sample(list(courses), 10)

    while count_courselist_totalviolations(course_lst)[0] != 0:
		# delete biggest violation course from course_lst
        (number_of_violations, violation_list) = count_courselist_totalviolations(course_lst)
        del_class_index = violation_list.index(max(violation_list))
        deleted_class = course_lst[del_class_index]
        course_lst.remove(deleted_class)
		# loop through courses not in course_lst such that adding it doesn't add violation or violation decreases
        # add first one found
        course_names = courses.keys()[:]
        random.shuffle(course_names)
        for course in course_names:
            if course != deleted_class and course not in course_lst:
                course_lst.append(course)
                if count_courselist_totalviolations(course_lst)[0] < number_of_violations:
                    break
                else:
                    course_lst.remove(course)
        # next iteration of while loop
        
    return course_lst


def simulated_annealing():
    course_lst = random.sample(list(courses), 10)

    return course_lst
