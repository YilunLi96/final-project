from readdata import *
import random

NUM_COURSES = 10

courses = read_catalog()

counts = dict()
counts['linalg'] = 1
counts['calc'] = 1
counts['basic'] = 2
counts['boaz'] = 1
counts['theory'] = 1
counts['breadth'] = 2
counts['tech'] = 2


def get_prereqs(course):
    "list of prereqs for a particular course"
    sem, p, sat = courses[course]
    return p


def get_requirements(course):
    "list of requirements this course fulfills"
    sem, p, sat = courses[course]
    return sat


def get_semesters(course):
    "list of semesters that the course is offered"
    sem, p, sat = courses[course]
    return sem


def distribute_courses_to_req(classes):
	"given a list of courses, distribute the courses to different requirements"
	
	reqs = ['linalg', 'calc', 'basic', 'boaz', 'theory', 'breadth', 'tech']
	course_list = classes[:]

	course_satisfied_reqs_lst = []
	
	for course in course_list:
		reqs_satisfied = get_requirements(course)
		if len(reqs_satisfied) == 1:
			course_satisfied_reqs_lst.append((course, reqs_satisfied[0]))
		else:
			requirement_satisfied = ''
			for req in reqs_satisfied:
				if req != 'tech':
					requirement_satisfied = req

			course_satisfied_reqs_lst.append((course, requirement_satisfied))
	return course_satisfied_reqs_lst


def countViolations(class_id, classes):
    violations = 0

    class_req_count = dict()

    classes_list = distribute_courses_to_req(classes)

    # calculate the requirements fulfilled by the course selection (classes)
    for (course, req) in classes_list:
		if req in class_req_count:
			class_req_count[req] += 1
		else:
			class_req_count[req] = 1

    # if the sum for a requirement is too large, violation plus 1
    for req in class_req_count:
    	if class_req_count[req] > counts[req]:
    		if (class_id, req) in classes_list:
    			violations += 1

    # prereq not present
    prereqs = get_prereqs(class_id)

    if prereqs != ['None']:
	    # for each prerequisite, check that it is present
	    for i in prereqs:
	        flag = 0
	        # loop over all classes
	        for j in classes:
	            # prereq is present in the schedule
	            if i == j:
	                flag = 1

	        if flag == 0:
	            violations += 1

    # duplicates
    dups = classes.count(class_id)
    dups -= 1
    violations += dups

    return violations


def count_courselist_totalviolations(list_of_courses):
    violations = 0
    vio_list = []
    for course in list_of_courses:
        v = countViolations(course, list_of_courses)
        violations += v
        vio_list.append(v)
    return (violations, vio_list)

## helper functions and set_up for CSP

# 0, make a copy of the course catalog
catalog = read_catalog()
reqs = ['linalg', 'calc', 'basic', 'basic', 'boaz', 'theory', 'tech', 'tech', 'breadth', 'breadth']


# gives the index of the next class to fill in
def next_class_to_fill(c_list):
    # search across the schedule and return class_id of first zero
    for class_id in xrange(0, NUM_COURSES):
        var = c_list[class_id]
        if var == 0:
            return class_id

    # otherwise return none
    return None


# tells whether a given course list is fully assigned
def course_list_complete(c_list):
    return next_class_to_fill(c_list) == None


# allowing duplicates returns list of classes that satisfy the requirement located at class_id
def valid_options(class_id):
    requirement_to_fill = reqs[class_id]
    course_list = []

    for course in catalog:
        if requirement_to_fill in get_requirements(course):
            course_list.append(course)
    random.shuffle(course_list)
    return course_list


# returns true if there are no violations or prereqs, otherwise false
# no need to check from requirements since we know the order they are satisfied in
def no_violations(c_list, course):
    prereq_list = get_prereqs(course)
    for pre in prereq_list:
        if pre not in c_list:
            return False
    return True

def sort_class(classes):
    classes = distribute_courses_to_req(classes)
    return classes
