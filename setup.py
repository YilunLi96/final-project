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

NUM_COURSES = 10


random.seed(18)  # IMPORTANT: DO NOT REMOVE!


def crossOff(values, nums):
    """
    Removes seen courses from domain values (removes all the elements in values
    that are also in nums).
    Also counts the possible constraint violations.
    """
    violations = 0
    for n in nums:
        # executes if n is not zero, or none
        if n:
            if not values[n-1]:
                violations += 1
            values[n-1] = None
    return violations

class Course:
    def __init__(self, schedule, courses, lastChanged=[], isFirstLocal=False, ):
        # array of size NUM_COURSES corresponding to the 12  courses that will be take type str
        self.schedule = schedule
        self.requirement_chosen = range(NUM_COURSES)

        # dictionary of courses with all relevant information
        self.courses = courses

        # list of classes that can still be taken
        self.classes_remaining = {}


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
        p, sat, sem = self.courses[course]
        return p

    def get_requirements(self, course):
        "list of requirements this course fulfills"
        p, sat, sem = self.courses[course]
        return sat

    def get_semesters(self, course):
        "list of semesters that the course is offered"
        p, sat, sem = self.courses[course]
        return sem

    def get_schedule(self):
    "current schedule"
    return list(self.schedule)

    def setVariable(self, class_id, name):
        """
        Creates a new version of the schedule with a certain class slot set to
        name
        """
        newSchedule = deepcopy(self.schedule)
        newSchedule[class_id] = name
        return Course(newSchedule, self.courses, [class_id])

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
        return self.firstEpsilonVariable() == None

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
        values = self.get_schedule()
        new_labels = self.courses.keys()

        self.class_conflicts[class_id] = crossOff(new_labels,values)
        self.classes_remaining[class_id] = new_labels

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
        possible_boards = []
        nextVariable =  self.nextVariable()

        # get domain for next variable
        dom = self.variableDomain(nextVariable[0],nextVariable[1])

        # loop over possible values for that variable
        for num in dom:
            temp_board = self.setVariable(nextVariable[0],nextVariable[1],num)
            possible_boards.append(temp_board)

        return possible_boards

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
        for i in xrange(0,9):
            for j in xrange(0,9):
                if self.board[i][j] == 0:
                    if self.variableDomain(i,j) == []:
                        return False

        return True

    # LOCAL SEARCH CODE
    # Fixed variables cannot be changed by the player.
    def _initLocalSearch(self):
        """
        Variables for keeping track of inconsistent, complete
        assignments. (Complete assignment formulism)
        """

        # For local search. Remember the fixed numbers.
        self.fixedVariables = {}
        for r in xrange(0, 9):
            for c in xrange(0, 9):
                if self.board[r][c]:
                    self.fixedVariables[r, c] = True
        self.updateAllFactors()

    def modifySwap(self, square1, square2):
        """
        Modifies the sudoku board to swap two
        row variable assignments.
        """
        t = self.board[square1[0]][square1[1]]
        self.board[square1[0]][square1[1]] = \
            self.board[square2[0]][square2[1]]
        self.board[square2[0]][square2[1]] = t

        self.lastMoves = [square1, square2]
        self.updateVariableFactors(square1)
        self.updateVariableFactors(square2)

    def numConflicts(self):
        "Returns the total number of conflicts"
        return sum(self.class_conflicts)

    # # PART 5
    # def randomRestart(self):
    #     """
    #     IMPLEMENT FOR PART 5
    #     Randomly initialize a complete, potentially inconsistent board, making
    #     sure that all row factors are being held consistent.  Meaning,
    #     the board may be inconsistent, but every row must contain each of the
    #     numbers in the domain.  Also make sure that you check before assigning
    #     a number to a position that a number isn't ALREADY assigned there!

    #     NOTE: Please, please, please use random.shuffle() -- will help us out
    #           on the autograder side!
    #     """
    #     # loop over rows
    #     for i in xrange(0,9):
    #         temp_list = range(1,10)

    #         # check what nums we need to shuffle
    #         vals = self.row(i)
    #         for j in vals:
    #             if j != 0:
    #                 temp_list.remove(j)

    #         # shuffle those nums
    #         random.shuffle(temp_list)

    #         # insert those nums
    #         for j in xrange(0,9):
    #             if vals[j] == 0:
    #                 self.board[i][j] = temp_list[0]
    #                 temp_list.pop(0)

    #     self.updateAllFactors() # to call at end of function
    #     return


    # # PART 6
    # def randomSwap(self):
    #     """
    #     IMPLEMENT FOR PART 6
    #     Returns two random variables that can be swapped without
    #     causing a row factor conflict.
    #     i.e. return (r0, c0), (r1, c1) if v0 and v1 are two non fixed variables
    #     that can be swapped without causing any row inconsistencies.

    #     NOTE: DO NOT swap any of the variables already set: fixedVariables
    #     """

    #     # keep choosing two variables without replacement and ensure none fixed
    #     flag = True
    #     r, c1, c2 = 0,0,0
    #     while flag:
    #         # choose random row, inside loop ensures doesn't spin on one row
    #         r, c1, c2 = random.randint(0,8), random.randint(0,8), random.randint(0,8)

    #         if (r,c1) not in self.fixedVariables and (r,c2) not in self.fixedVariables:
    #             flag = False

    #     return (r,c1), (r,c2)


    # # PART 7
    # def gradientDescent(self, variable1, variable2):
    #     """
    #     IMPLEMENT FOR PART 7
    #     Decide if we should swap the values of variable1 and variable2.
    #     """
    #     a,b = variable1
    #     c,d = variable2
    #     # create new board with switched vars
    #     board1 = self.setVariable(a,b,self.board[c][d])
    #     board2 = board1.setVariable(c,d,self.board[a][b])
    #     board2.updateAllFactors()

    #     # check num of conflicts in each board, execute swap if viols lower
    #     if board2.numConflicts() <= self.numConflicts():
    #         self.modifySwap(variable1,variable2)
    #         return
    #     else:
    #         # case where f is higher use probs
    #         if random.random() <= 0.001:
    #             self.modifySwap(variable1,variable2)

    #         return





########## RUNS THE CSP AND SOLVES FOR SCHEDULE ##########
def main(arguments):
    global start, args
    set_args(arguments)
    start = Sudoku(boardEasy if args.easy else boardHard,
                   isFirstLocal=args.localsearch)

    print args

    setup = '''
from __main__ import start, solveLocal, solveCSP
'''
    solveSudoku = '''
print 'Solution: ' + str(solveCSP(start))
'''
    solveSudokuLocal = '''
print 'Solution: ' + str(solveLocal(start))
'''

    print 'Time elapsed: ' + str(timeit.timeit(
            solveSudokuLocal if args.localsearch else solveSudoku,
            setup=setup, number=1))


