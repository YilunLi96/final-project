from readdata import *

NUM_COURSES = 10

courses = read_catalog()

counts = dict()
counts['linalg'] = 1
counts['calc'] = 1
counts['basic'] = 2
counts['boaz'] = 1
counts['theory'] = 1
counts['tech'] = 2
counts['breadth'] = 2


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

def countViolations(class_id, classes):
    violations = 0

    # if the sum for that requirement is too large
    reqs = self.get_reqs()
    req = reqs[class_id]
    ctr = 0
    for i in reqs:
        if i == req and class_id != i:
            ctr += 1
    if ctr > self.requirement_counts[req]:
        violations += 1

    # prereq not present
    sched = self.get_schedule()
    prereqs = self.get_prereqs(sched[class_id])

    # for each prerequisite, check that it is present
    for i in prereqs:
        flag = 0

        # loop over items prior to this class in schedule
        for j in xrange(0,class_id):
            # prereq is present in the schedule
            if i == sched[j]:
                flag = 1

        if flag == 0:
            violations += 1

    # duplicates
    dups = sched.count(sched[class_id])
    dups -= 1
    violations += dups

    return violations


print get_prereqs('CS182')
print get_requirements('CS182')