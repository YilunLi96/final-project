from readdata import *
from localsearch import *
from CSP import *
from readdata import *
from course_setup import *


# Important: prefers classes with less pre_reqs!
def iterative_less_conflicts_have_to_take():
    course_lst = []
    for course in specified_courses:
        if specified_courses[course][3] == 1:
            course_lst.append(course)
    for course in course_lst:
		# print course
        if get_prereqs(course) != ['None']:
            course_lst += get_prereqs(course)

    if honor_flag == 1:
        additional_lst = random.sample(list(courses), 10 - len(course_lst))
    else:
        additional_lst = random.sample(list(courses), 12 - len(course_lst))

    total_list = course_lst + additional_lst

    while count_courselist_totalviolations(total_list)[0] != 0:
		# delete biggest violation course from course_lst
        (number_of_violations, violation_list) = count_courselist_totalviolations(total_list)

        maxi_index = 0
        maxi = -99999.
        for i in range(len(course_lst), len(total_list)):
        	if violation_list[i] > maxi:
        		maxi = violation_list[i]
        		maxi_index = i

        deleted_class = total_list[maxi_index]

        if deleted_class not in additional_lst:
        	total_list.remove(deleted_class)
        	additional_lst = [x for x in total_list if x not in course_lst]


        additional_lst.remove(deleted_class)
        total_list.remove(deleted_class)
		# loop through courses not in course_lst such that adding it doesn't add violation or violation decreases
        # add first one found
        course_names = courses.keys()[:]
        random.shuffle(course_names)
        for course in course_names:
            if course != deleted_class and course not in total_list:
                additional_lst.append(course)
                total_list.append(course)
                if count_courselist_totalviolations(total_list)[0] < number_of_violations:
                    break
                else:
                    additional_lst.remove(course)
                    total_list.remove(course)
        # next iteration of while loop
    # print count_courselist_totalviolations(total_list)[0]
    return total_list


def set_CSP_initial():
    CSP_initial_lst = CSP_initial[:]

    course_lst = []
    for course in specified_courses:
        if specified_courses[course][3] == 1:
            course_lst.append(course)
    for course in course_lst:
		# print course
        if get_prereqs(course) != ['None']:
            course_lst += get_prereqs(course)

    for i in range(len(reqs)):
    	for course in course_lst:
    		if course in CSP_initial_lst:
    			continue
    		if reqs[i] in get_requirements(course):
    			# print reqs[i], course
    			CSP_initial_lst[i] = course
    			break
    
    return  CSP_initial_lst

# print set_CSP_initial()

