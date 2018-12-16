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
    trials = 15

    # variable for how many top frequent courses to show
    top_courses = 15

    # lists to hold list of courses
    iterative = []
    sim_an = []
    back = []

    # run the code to gather the course data
    for i in xrange(0,50):
        iterative.extend(iterative_less_conflicts())
        sim_an.extend(simulated_annealing())
        back.extend(backtracking(CSP_initial))

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
    print "done"

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
    print "done"

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
    print "done"

# make the graphs
# group_one_most_frequent()



def group_one_run_times():
    trials = 50

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


    # simulated annealing runs
    t0 = time.clock()
    for i in range(trials): simulated_annealing()
    t1 = time.clock()

    s_time = t1-t0
    s_average = s_time / float(trials)
    run_times.append(s_average)


    # backtracking runs
    t0 = time.clock()
    for i in range(trials): backtracking(CSP_initial)
    t1 = time.clock()

    b_time = t1-t0
    b_average = b_time / float(trials)
    run_times.append(b_average)

    # make graph of run times

    return run_times

print group_one_run_times()



#### Histograms of Most Popular Courses ####

# GROUP TWO
# 0. on the graph, title needs to include that this is for non-honor track
# 0.5 title includes that in this example, the must-takes are: 182, 124, 61
# 1. run each of the following three () a bunch of iterations (1000? 10000?), then compare speed of each
# 2. out of those iterations, for each funtion, draw the histogram of the most frequent courses
# iterative_less_conflicts_have_to_take()
# backtracking(set_CSP_initial())

# GROUP THREE
# 1. run a bunch of iterations (1000? 10000?), then calculate speed
# 2. simulated_annealing_weighted()[1] is the utility, calculate the expected utility out of those iterations
# simulated_annealing_weighted()
