from readdata import *
from localsearch import *
from CSP import *
from readdata import *
from course_setup import *


def simulated_annealing_weighted():
    if honor_flag == 1:
    	course_lst = random.sample(list(courses), 10)
    else:
    	course_lst = random.sample(list(courses), 12)

    T = 1000.

    DECAY = 0.98
    counter = 0

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
    	if new_num_violations < number_of_violations and total_utility(temp_list) > total_utility(course_lst):
    		course_lst = temp_list
    	else:
            if new_num_violations >= number_of_violations and total_utility(temp_list) <= total_utility(course_lst):
                if random.random() <= math.exp((number_of_violations - new_num_violations + total_utility(temp_list) - total_utility(course_lst)) / T):
                    course_lst = temp_list
                else:
    			    course_lst = course_lst
            elif new_num_violations >= number_of_violations and total_utility(temp_list) > total_utility(course_lst):
                if random.random() <= math.exp((number_of_violations - new_num_violations) / T):
                    course_lst = temp_list
                else:
                    course_lst = course_lst
            else:
                if random.random() <= math.exp((total_utility(temp_list) - total_utility(course_lst)) / T):
                    course_lst = temp_list
                else:
                    course_lst = course_lst

    	# update temprature
    	T *= DECAY
        counter += 1

        # random restart to get out (sometimes we pursue utility but got stuck a place where no successor satisfies the constraint)
        if counter == 1000:
            if honor_flag == 1:
                course_lst = random.sample(list(courses), 10)
            else:
                course_lst = random.sample(list(courses), 12)

            T = 1000.
            counter = 0


    return course_lst, total_utility(course_lst)

def CSP_uniform_cost_reverse():
    return course_lst, total_utility(course_lst)