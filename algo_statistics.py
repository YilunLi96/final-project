from localsearch import *
from CSP import *
from course_setup import *
from weighted_courses import *
from have_to_take import *
import collections
import numpy as np
import matplotlib.pyplot as plt
import time


# GROUP ONE
# 0. on the graph, title needs to include that this is for non-honor track
# 1. run each of the following three () a bunch of iterations (1000? 10000?), then compare speed of each
# 2. out of those iterations, for each funtion, draw the histogram of the most frequent courses
# iterative_less_conflicts()
# simulated_annealing()
# backtracking(CSP_initial)

def group_one_most_frequent():
    # iterations to run
    trials = 1000

    # variable for how many top frequent courses to show
    top_courses = 15

    # lists to hold list of courses
    iterative = []
    sim_an = []
    back = []

    # run the code to gather the course data
    for i in xrange(0,trials):
        iterative.extend(iterative_less_conflicts())
        sim_an.extend(simulated_annealing())
        back.extend(backtracking(CSP_initial))
    print "done running -> more stuff now"

    # form counts from the list of classes
    i_counter = collections.Counter(iterative)
    s_counter = collections.Counter(sim_an)
    b_counter = collections.Counter(back)

    # get top frequencies
    i_top = i_counter.most_common(top_courses)
    s_top = s_counter.most_common(top_courses)
    b_top = b_counter.most_common(top_courses)

    # unpack into two lists
    i_courses, i_count = map(list, zip(*i_top))
    s_courses, s_count = map(list, zip(*s_top))
    b_courses, b_count = map(list, zip(*b_top))

    # iterative bar chart
    y_pos = np.arange(len(i_courses))

    plt.bar(y_pos, i_count, align='center', alpha=0.5)
    plt.xticks(y_pos, i_courses, rotation=45)
    plt.ylabel('Frequency')
    plt.title('Iterative Top Courses (Non-honors)')
    plt.xlabel('Course Name')
    plt.tight_layout()

    plt.savefig('g_one_iter.png')
    plt.gcf().clear()

    # iterative bar chart
    y_pos = np.arange(len(s_courses))

    plt.bar(y_pos, s_count, align='center', alpha=0.5)
    plt.xticks(y_pos, s_courses, rotation=45)
    plt.ylabel('Frequency')
    plt.title('Simulated Annealing Top Courses (Non-honors)')
    plt.xlabel('Course Name')
    plt.tight_layout()

    plt.savefig('g_one_sa.png')
    plt.gcf().clear()

    # iterative bar chart
    y_pos = np.arange(len(b_courses))

    plt.bar(y_pos, b_count, align='center', alpha=0.5)
    plt.xticks(y_pos, b_courses, rotation=45)
    plt.ylabel('Frequency')
    plt.title('Backtracking Top Courses (Non-honors)')
    plt.xlabel('Course Name')
    plt.tight_layout()

    plt.savefig('g_one_back.png')
    plt.gcf().clear()

# make the graphs
# group_one_most_frequent()
# print "DONE GROUP 1.1"


def group_one_run_times():
    trials = 1000

    # only need to know the total time it takes to run, which can then be average
    # iterative -> simulated annealing -> backtracking
    run_times = []

    # iterative runs
    t0 = time.clock()
    for i in range(trials): iterative_less_conflicts()
    t1 = time.clock()

    i_time = t1-t0
    i_average = i_time / float(trials)
    run_times.append(i_average)
    print "done"


    # simulated annealing runs
    t0 = time.clock()
    for i in range(trials): simulated_annealing()
    t1 = time.clock()

    s_time = t1-t0
    s_average = s_time / float(trials)
    run_times.append(s_average)
    print "done"


    # backtracking runs
    t0 = time.clock()
    for i in range(trials): backtracking(CSP_initial)
    t1 = time.clock()

    b_time = t1-t0
    b_average = b_time / float(trials)
    run_times.append(b_average)
    print "done"

    # take the log of the run times for graphing
    log_times = np.log10(run_times)

    # make graph of run times
    y_pos = np.arange(3)
    methods = ['Iter.', 'SA', 'Back.']

    plt.bar(y_pos, log_times, align='center', alpha=0.5)
    plt.xticks(y_pos, methods, rotation=45)
    plt.ylabel('Run Time in Log 10 (seconds)')
    plt.title('Run Time Log Comparison (Non-honors)')
    plt.xlabel('Course Planning Method')
    plt.tight_layout()

    plt.savefig('g_one_logtimes.png')
    plt.gcf().clear()

    plt.bar(y_pos, run_times, align='center', alpha=0.5)
    plt.xticks(y_pos, methods, rotation=45)
    plt.ylabel('Run Time (seconds)')
    plt.title('Run Time Comparison (Non-honors)')
    plt.xlabel('Course Planning Method')
    plt.tight_layout()

    plt.savefig('g_one_times.png')
    plt.gcf().clear()

    return run_times
# print "\n\n"
# print group_one_run_times()
# print "DONE GROUP 1.2"


# GROUP TWO
# 0. on the graph, title needs to include that this is for non-honor track
# 0.5 title includes that in this example, the must-takes are: 182, 124, 61
# 1. run each of the following three () a bunch of iterations (1000? 10000?), then compare speed of each
# 2. out of those iterations, for each funtion, draw the histogram of the most frequent courses
# iterative_less_conflicts_have_to_take()
# backtracking(set_CSP_initial())

def group_two_most_frequent():
    # iterations to run
    trials = 1000

    # variable for how many top frequent courses to show
    top_courses = 15

    # lists to hold list of courses
    iterative = []
    back = []

    # run the code to gather the course data
    for i in xrange(0,trials):
        iterative.extend(iterative_less_conflicts_have_to_take())
        back.extend(backtracking(set_CSP_initial()))
    print "done running -> more stuff now"

    # form counts from the list of classes
    i_counter = collections.Counter(iterative)
    b_counter = collections.Counter(back)

    # get top frequencies
    i_top = i_counter.most_common(top_courses)
    b_top = b_counter.most_common(top_courses)

    # unpack into two lists
    i_courses, i_count = map(list, zip(*i_top))
    b_courses, b_count = map(list, zip(*b_top))

    # iterative bar chart
    y_pos = np.arange(len(i_courses))

    plt.bar(y_pos, i_count, align='center', alpha=0.5)
    plt.xticks(y_pos, i_courses, rotation=45)
    plt.ylabel('Frequency')
    plt.title('Iterative Top Courses w CS 182/124/61 (Non-honors)')
    plt.xlabel('Course Name')
    plt.tight_layout()

    plt.savefig('g_two_iter.png')
    plt.gcf().clear()

    #  backtracking bar chart
    y_pos = np.arange(len(b_courses))

    plt.bar(y_pos, b_count, align='center', alpha=0.5)
    plt.xticks(y_pos, b_courses, rotation=45)
    plt.ylabel('Frequency')
    plt.title('Backtracking Top Courses w CS 182/124/61 (Non-honors)')
    plt.xlabel('Course Name')
    plt.tight_layout()

    plt.savefig('g_two_back.png')
    plt.gcf().clear()

# make the graphs
# group_two_most_frequent()
# print "DONE GROUP 2.1"

def group_two_run_times():
    trials = 1000

    # only need to know the total time it takes to run, which can then be average
    # iterative -> simulated annealing -> backtracking
    run_times = []

    # iterative runs
    t0 = time.clock()
    for i in range(trials): iterative_less_conflicts_have_to_take()
    t1 = time.clock()

    i_time = t1-t0
    i_average = i_time / float(trials)
    run_times.append(i_average)
    print "done"

    # backtracking runs
    t0 = time.clock()
    for i in range(trials): backtracking(set_CSP_initial())
    t1 = time.clock()

    b_time = t1-t0
    b_average = b_time / float(trials)
    run_times.append(b_average)
    print "done"

    # take the log of the run times for graphing
    log_times = np.log10(run_times)

    # make graph of run times
    y_pos = np.arange(2)
    methods = ['Iter.', 'Back.']

    plt.bar(y_pos, log_times, align='center', alpha=0.5)
    plt.xticks(y_pos, methods, rotation=45)
    plt.ylabel('Run Time in Log 10 (seconds)')
    plt.title('Run Time Log Comparison w CS 182/124/61 (Non-honors)')
    plt.xlabel('Course Planning Method')
    plt.tight_layout()

    plt.savefig('g_two_logtimes.png')
    plt.gcf().clear()

    plt.bar(y_pos, run_times, align='center', alpha=0.5)
    plt.xticks(y_pos, methods, rotation=45)
    plt.ylabel('Run Time (seconds)')
    plt.title('Run Time Comparison w CS 182/124/61 (Non-honors)')
    plt.xlabel('Course Planning Method')
    plt.tight_layout()

    plt.savefig('g_two_times.png')
    plt.gcf().clear()

    return run_times
# print "\n\n"
# print group_two_run_times()
# print "DONE GROUP 2.2"

# GROUP THREE
# 1. run a bunch of iterations (1000? 10000?), then calculate speed
# 2. simulated_annealing_weighted()[1] is the utility, calculate the expected utility out of those iterations
# simulated_annealing_weighted()

def group_three_most_frequent():
    # iterations to run
    trials = 1000

    # variable for how many top frequent courses to show
    top_courses = 15

    # lists to hold list of courses
    sa = []
    utilities = []

    # run the code to gather the course data
    t0 = time.clock()
    for i in xrange(0,trials):
        a,b = simulated_annealing_weighted()
        sa.extend(a)
        utilities.append(b)
    t1 = time.clock()

    s_time = t1-t0
    s_average = s_time / float(trials)
    print "Average Runtime is: " + str(s_average)
    print "done running -> more stuff now"

    # form counts from the list of classes
    s_counter = collections.Counter(sa)

    # get top frequencies
    s_top = s_counter.most_common(top_courses)

    # unpack into two lists
    s_courses, s_count = map(list, zip(*s_top))

    # simulated annealing bar chart
    y_pos = np.arange(len(s_courses))

    plt.bar(y_pos, s_count, align='center', alpha=0.5)
    plt.xticks(y_pos, s_courses, rotation=45)
    plt.ylabel('Frequency')
    plt.title('Simulated Annealing Maximizing Utility (Non-honors)')
    plt.xlabel('Course Name')
    plt.tight_layout()

    plt.savefig('g_three_sa.png')

    # calculate total utility
    total = sum(utilities) / float(len(utilities))
    print "Total Expected Utility is: " + str(total)


# make the graphs
# group_three_most_frequent()
# print "DONE GROUP 3.1"


# # GROUP 3.2
def group_four_most_frequent():
    # iterations to run
    trials = 100

    # variable for how many top frequent courses to show
    top_courses = 15

    # lists to hold list of courses
    sa = []
    utilities = []

    # run the code to gather the course data
    t0 = time.clock()
    for i in xrange(0,trials):
        a,b = CSP_uniform_cost_weighted(CSP_initial2)
        sa.extend(a)
        utilities.append(b)
    t1 = time.clock()

    s_time = t1-t0
    s_average = s_time / float(trials)
    print "Average Runtime is: " + str(s_average)
    print "done running -> more stuff now"

    # form counts from the list of classes
    s_counter = collections.Counter(sa)

    # get top frequencies
    s_top = s_counter.most_common(top_courses)

    # unpack into two lists
    s_courses, s_count = map(list, zip(*s_top))

    # simulated annealing bar chart
    y_pos = np.arange(len(s_courses))

    plt.bar(y_pos, s_count, align='center', alpha=0.5)
    plt.xticks(y_pos, s_courses, rotation=45)
    plt.ylabel('Frequency')
    plt.title('Weighted Uniform Cost (Non-honors)')
    plt.xlabel('Course Name')
    plt.tight_layout()

    plt.savefig('g_three_uni.png')

    # calculate total utility
    total = sum(utilities) / float(len(utilities))
    print "Total Expected Utility is: " + str(total)

group_four_most_frequent()


# CSP_uniform_cost_weighted(CSP_initial2)
