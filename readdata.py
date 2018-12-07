
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

# print catalog
# print catalog['ES170']
# print catalog['CS134']