#########################################
#########################################
#########################################
#### CS 182 FINAL PROJECT
#### AUTHORS: ERICK MEZA, YILUN LI
#### DECEMBER 2018
#########################################
#########################################
#########################################

from copy import deepcopy
import timeit
import os
import sys
import random
import argparse
import readdata

NUM_COURSES = 10


random.seed(18)  # IMPORTANT: DO NOT REMOVE!


class Course:
    def __init__(self, schedule, reqs, courses, lastChanged=[], isFirstLocal=False, ):
        # array of size NUM_COURSES corresponding to the 12  courses that will be take type str
        self.schedule = schedule
        self.requirement_chosen = reqs

        # dictionary of courses with all relevant information
        self.courses = courses

        # set up how many of each category requirement we need
        counts = dict()
        counts['linalg'] = 1
        counts['calc'] = 1
        counts['basic'] = 2
        counts['boaz'] = 1
        counts['theory'] = 1
        counts['tech'] = 2
        counts['breadth'] = 2

        self.requirement_counts = counts


        # The number of conflicts at a course slot (any of the 10)
        self.class_conflicts = {}

        # For local search. Keep track of the factor state.
        if isFirstLocal:
            self._initLocalSearch()

        self.lastChanged = lastChanged

    #### HELPER FUNCTIONS FOR COURSE PLANNER ####
    def get_prereqs(self, course):
        "list of prereqs for a particular course"
        sem, p, sat = self.courses[course]
        return p

    def get_requirements(self, course):
        "list of requirements this course fulfills"
        sem, p, sat = self.courses[course]
        return sat

    def get_semesters(self, course):
        "list of semesters that the course is offered"
        sem, p, sat = self.courses[course]
        return sem

    def get_reqs(self):
      "current requirements"
      return list(self.requirement_chosen)

    def get_schedule(self):
      "current schedule"
      return list(self.schedule)

    def countViolations(self, class_id):
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

    def setVariable(self, class_id, name):
        """
        Creates a new version of the schedule with a certain class slot set to
        name
        """
        newSchedule = deepcopy(self.schedule)
        newSchedule[class_id] = name

        # chooses one of the requirements to assign to that course
        newReqs = deepcopy(self.requirement_chosen)
        reqs = self.get_requirements(name)
        newReqs[class_id] = random.choice(reqs)
        return Course(newSchedule, newReqs, self.courses, [class_id])

    # PART 1
    def firstEpsilonVariable(self):
        """
        IMPLEMENT FOR PART 1
        Returns the first variable with assignment epsilon, otherwise return
        None (i.e. first square in the board that is unassigned -- 0).

        NOTE: for the sake of the autograder, please search for the first
        unassigned variable column-wise, then row-wise:
        for r in row:
            for c in col:
        """
        # search across the schedule and return class_id of first zero
        for class_id in xrange(0,NUM_COURSES):
            var = self.schedule[class_id]
            if var == 0:
              return class_id

        # otherwise return none
        return None


    def complete(self):
        """
        IMPLEMENT FOR PART 1
        Returns true if the assignment is complete

        i.e. if there are no more first epsilon variables
        """
        # call firstEpsilonVariable
        # return self.firstEpsilonVariable() == None
        return self.numConflicts() == 0 and self.firstEpsilonVariable() == None

    def variableDomain(self, class_id):
        """
        IMPLEMENT FOR PART 1
        Returns current domain for the class_id variable, and [] if the
        domain is empty.

        i.e. return a list of the possible class assignments to this variable
        without breaking consistency .
        """
        # keep track of elements that have been seen so far
        seen_classes = set()

        # elements in schedule
        for i in self.schedule:
            if i != 0:
                seen_classes.add(i)

        # result is subtracting seen elements from set of 1 to 9
        possible_classes = set(self.courses.keys())
        diff = possible_classes.difference(seen_classes)

        return list(diff)

    # PART 2
    def updateFactor(self, class_id):
        """
        IMPLEMENT FOR PART 2
        Update the values remaining for a factor.
        `factor_type` is one of BOX, ROW, COL
        `i` is an index between 0 and 8.

        i.e. update factorNumConflicts to contain the number of conflicts
        present at a factor (how many elements to remove to not be in conflict)
        and factorRemaining to contain the remaining numbers not yet assigned
        in the factor.

        conflicts for a specific course will only ever involve courses that
        precede it in the schedule
        """

        self.class_conflicts[class_id] = self.countViolations(class_id)

        return

    def updateAllFactors(self):
        """
        IMPLEMENT FOR PART 2
        Update the values remaining for all class slots
        """
        # call updateFactor on each factor
        for j in xrange(0,NUM_COURSES):
            self.updateFactor(j)

        return

    def updateVariableFactors(self):
        """
        IMPLEMENT FOR PART 2
        Update all the factors impacting a variable (neighbors in factor graph).
        """
        self.updateAllFactors()

        return

    # CSP SEARCH CODE
    def nextVariable(self):
        """
        Return the next variable to try assigning.
        """
        if args.mostconstrained:
            return self.mostConstrainedVariable()
        else:
            return self.firstEpsilonVariable()

    # PART 3
    def getSuccessors(self):
        """
        IMPLEMENT IN PART 3
        Returns new assignments with each possible value
        assigned to the variable returned by `nextVariable`.  If no valid
        assignments exist, return [].

        i.e. get the next variable to assign, and return a list of all possible
        boards, with that variable assigned to all possible values in its
        domain.

        Hint: setVariable and variableDomain will be useful
        """
        possible_schedules = []
        nextVariable =  self.nextVariable()

        # get domain for next variable
        dom = self.variableDomain(nextVariable)

        # loop over possible values for that variable
        for course in dom:
            temp_sched = self.setVariable(nextVariable,course)
            possible_schedules.append(temp_sched)

        return possible_schedules

    def getAllSuccessors(self):
        if not args.forward:
            return self.getSuccessors()
        else:
            return self.getSuccessorsWithForwardChecking()

    # PART 4
    def getSuccessorsWithForwardChecking(self):
        return [s for s in self.getSuccessors() if s.forwardCheck()]

    def forwardCheck(self):
        """
        IMPLEMENT IN PART 4
        Returns True if all variables have non-empty domains, o.w. False.

        i.e. make sure that for every unassigned element in the board, that
        element has a non-trivial domain (its domain isn't empty)
        """
        # loop over all variables, need to only check unassigned variables tho
        # for i in xrange(0,9):
        #     for j in xrange(0,9):
        #         if self.board[i][j] == 0:
        #             if self.variableDomain(i,j) == []:
        #                 return False

        # return True
        return

    # LOCAL SEARCH CODE
    # Fixed variables cannot be changed by the player.
    def _initLocalSearch(self):
        """
        Variables for keeping track of inconsistent, complete
        assignments. (Complete assignment formulism)
        """

        # For local search. Remember the fixed numbers.
        # self.fixedVariables = {}
        # for r in xrange(0, 9):
        #     for c in xrange(0, 9):
        #         if self.board[r][c]:
        #             self.fixedVariables[r, c] = True
        # self.updateAllFactors()
        return

    def modifySwap(self, cl_id, other, sat):
        """
        Modifies the sudoku board to swap two
        row variable assignments.
        """
        self.schedule[cl_id] = other
        self.requirement_chosen[cl_id] = sat

        self.updateAllFactors()


    def numConflicts(self):
        "Returns the total number of conflicts"
        return sum(self.class_conflicts.values())

    # PART 5
    def randomRestart(self):
        """
        IMPLEMENT FOR PART 5
        Randomly initialize a complete, potentially inconsistent board, making
        sure that all row factors are being held consistent.  Meaning,
        the board may be inconsistent, but every row must contain each of the
        numbers in the domain.  Also make sure that you check before assigning
        a number to a position that a number isn't ALREADY assigned there!

        NOTE: Please, please, please use random.shuffle() -- will help us out
              on the autograder side!
        """

        options = self.courses.keys()
        # hardcode testing
        classes = ['Math21a', 'Math21b', 'CS50', 'CS51', 'CS121', 'CS124', 'Stat110', 'CS134', 'CS136', 'CS181']
        reqs = ['calc', 'linalg', 'basic', 'basic', 'boaz', 'theory', 'tech', 'tech', 'breadth', 'breadth']

        # # loop over rows
        # for i in xrange(7,NUM_COURSES):
        #     # pick a random class
        #     cl = random.choice(options)

        #     # pick a requirement you want it to satisfy
        #     satisfies = self.get_requirements(cl)
        #     sat = random.choice(satisfies)

        #     classes.append(cl)
        #     reqs.append(sat)


        self.schedule = classes
        self.requirement_chosen = reqs


        self.updateAllFactors() # to call at end of function
        print self.numConflicts()


    # PART 6
    def randomSwap(self):
        """
        IMPLEMENT FOR PART 6
        Returns two random variables that can be swapped without
        causing a row factor conflict.
        i.e. return (r0, c0), (r1, c1) if v0 and v1 are two non fixed variables
        that can be swapped without causing any row inconsistencies.

        NOTE: DO NOT swap any of the variables already set: fixedVariables
        """

        # finds variable that can be switched out
        # possible = []
        # sched = self.get_schedule()
        # for i in sched:
        #     if self.class_conflicts[sched.index(i)] > 0:
        #         possible = i

        # if possible:
        #     cl = random.choice(possible)
        #     others = self.variableDomain(sched.index(cl))
        #     other = random.choice(others)
        #     return sched.index(cl), other
        # else:
        #     return None
        possible = 0
        sched = self.get_schedule()
        for i in sched:
            if self.class_conflicts[sched.index(i)] > 0:
                cl = i

        others = self.variableDomain(sched.index(cl))
        other = random.choice(others)
        return sched.index(cl), other


    # PART 7
    def gradientDescent(self, cl_id, other):
        """
        IMPLEMENT FOR PART 7
        Decide if we should swap the values of variable1 and variable2.
        """

        # create new board with switched vars
        board1 = self.setVariable(cl_id, other)
        board1.updateAllFactors()

        # check num of conflicts in each board, execute swap if viols lower
        if board1.numConflicts() <= self.numConflicts():
            self.modifySwap(cl_id, other, board1.requirement_chosen[cl_id])
            return
        else:
            # case where f is higher use probs
            if random.random() <= 0.001:
                self.modifySwap(cl_id, other, board1.requirement_chosen[cl_id])

            return


########## SOLVE CSP ###############
def solveCSP(problem):
    statesExplored = 0
    frontier = [problem]
    while frontier:
        state = frontier.pop()

        statesExplored += 1
        if state.complete():
            print 'Number of explored: ' + str(statesExplored)
            return state.get_schedule()
        else:
            successors = state.getAllSuccessors()
            if args.debug:
                if not successors:
                    print "DEADEND BACKTRACKING \n"
            frontier.extend(successors)

        if args.debug:
            os.system("clear")
            print state
            raw_input("Press Enter to continue...")

        # if args.debug_ipython:
        #     from time import sleep
        #     from IPython import display
        #     display.display(display.HTML(state.prettyprinthtml()))
        #     display.clear_output(True)
        #     sleep(0.5)

    return None


#########  SOLVE LOCAL ###############
def solveLocal(problem):
    for r in range(1):
        problem.randomRestart()
        state = problem
        originalConflicts = 0
        for i in range(100000):
            originalConflicts = state.numConflicts()

            cl_id, other = state.randomSwap()

            state.gradientDescent(cl_id, other)

            # if args.debug_ipython:
            #     from time import sleep
            #     from IPython import display
            #     state.lastMoves = [s1, s2]
            #     display.display(display.HTML(state.prettyprinthtml()))
            #     display.clear_output(True)
            #     sleep(0.5)

            if state.numConflicts() == 0:
                return state
                break

            if args.debug:
                os.system("clear")
                print state
                raw_input("Press Enter to continue...")
        print "Conflicts left: " + str(originalConflicts)

# schedule = [0] * NUM_COURSES
# reqs = [0] * NUM_COURSES
# courses = readdata.read_catalog()

# start = Course(schedule, reqs, courses)

# print 'Solution: ' + str(solveCSP(start))

def set_args(arguments):
    global start, args
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--easy', default=False, help="Use easy board.")
    parser.add_argument('--debug', default=False, help="Print each state.")
    parser.add_argument('--debug_ipython', default=False,
                        help="Print each state in html.")

    parser.add_argument('--localsearch', default=False,
                        help="Use local search.")
    parser.add_argument('--mostconstrained', default=False,
                        help="Use most constrained heuristic.")
    parser.add_argument('--forward', default=False,
                        help="Use forward checking.")
    parser.add_argument('--time', default=False)

    args = parser.parse_args(arguments)

start = None
args = None
schedule = [0] * NUM_COURSES
reqs = [0] * NUM_COURSES
courses = readdata.read_catalog()


######### RUNS THE CSP AND SOLVES FOR SCHEDULE ##########
def main(arguments):
    global start, args
    set_args(arguments)
    # schedule = [0] * NUM_COURSES
    # reqs = [0] * NUM_COURSES
    # courses = readdata.read_catalog()

    start = Course(schedule, reqs, courses, isFirstLocal=args.localsearch)

    # print 'Solution: ' + str(solveCSP(start))

    print args

    setup = '''
from __main__ import start, solveLocal, solveCSP
'''
    solveSchedule = '''
print 'Solution: ' + str(solveCSP(start))
'''
    solveScheduleLocal = '''
print 'Solution: ' + str(solveLocal(start))
'''
    print solveLocal(start)

    print 'Time elapsed: ' + str(timeit.timeit(
            solveScheduleLocal if args.localsearch else solveSchedule,
            setup=setup, number=1))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
