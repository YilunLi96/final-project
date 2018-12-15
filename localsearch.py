from readdata import *
from course_setup import *
import random
import math


# Important: prefers classes with less pre_reqs!
def iterative_less_conflicts():
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
    T = 1000

    DECAY = 0.98

    while count_courselist_totalviolations(course_lst)[0] != 0:
    	# compute violations of the initial course_lst
    	(number_of_violations, violation_list) = count_courselist_totalviolations(course_lst)

    	# make a copy of course list
    	temp_list = course_lst[:]

    	# pick a random successor
    	random_delete = random.choice(temp_list)
    	temp_list.remove(random_delete)
    	random_course = random.sample(list(courses), 1)
    	while random_course[0] in temp_list or random_course[0] == random_delete:
    		random_course = random.sample(list(courses), 1)
    	temp_list.append(random_course[0])

    	# test if we accept the new list
    	new_num_violations = count_courselist_totalviolations(temp_list)[0]
    	if new_num_violations < number_of_violations:
    		course_lst = temp_list
    	else:
    		if random.random() <= math.exp((number_of_violations - new_num_violations) / T):
    			course_lst = temp_list
    		else:
    			course_lst = course_lst

    	# update temprature
    	T *= DECAY


    return course_lst



