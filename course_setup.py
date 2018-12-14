from readdata import *


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


def sort_class(classes):
    classes = distribute_courses_to_req(classes)

    return classes
