def read_catalog():
    catalog = {}

    with open('course_names.csv') as nw_file:
        counter = 0
        for line in nw_file:
            counter += 1
            arr = line.split(',')
            if counter == 1:
                continue
            catalog[arr[0]] = (arr[1],)

    with open('pre_req.csv') as nw_file:
        counter = 0
        for line in nw_file:
            counter += 1
            arr = line.split(',')
            if counter == 1:
                continue
            lst = []
            for i in range(1, len(arr)):
            	lst.append(arr[i])
            del lst[-1]
            if lst[-1] == ' ':
            	del lst[-1]
            if arr[0] in catalog:
            	catalog[arr[0]] = catalog[arr[0]] + (lst,)

    with open('satisfy_req.csv') as nw_file:
        counter = 0
        for line in nw_file:
            counter += 1
            arr = line.split(',')
            if counter == 1:
                continue
            lst = []
            for i in range(1, len(arr)):
            	lst.append(arr[i])
            del lst[-1]
            if lst[-1] == ' ':
            	del lst[-1]
            if arr[0] in catalog:
            	catalog[arr[0]] = catalog[arr[0]] + (lst,)

    return catalog

def weighted_read_catalog():
    catalog = read_catalog()
    for course in catalog:
        catalog[course] += (0.1,)
    return catalog

# print weighted_read_catalog()

def set_weighting(course, weight, catalog):
    lst = list(catalog[course])
    lst[3] = weight
    catalog[course] = tuple(lst)

# weighted_courses = weighted_read_catalog()
# set_weighting('CS182', 1, weighted_courses)

# print weighted_courses['CS182']
