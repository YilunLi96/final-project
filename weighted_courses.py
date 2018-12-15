from readdata import *
from localsearch import *
from CSP import *
from readdata import *
from course_setup import *

courses_catalog = read_catalog()

def simulated_annealing_weighted():
    if honor_flag == 1:
    	course_lst = random.sample(list(courses), 10)
    else:
    	course_lst = random.sample(list(courses), 12)

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
