n = int(input())

# creating a list of sets.
if n != 0:
    i = 0
    sets = []
    while i < n:
        new_set = set()
        for e in input().split():
            new_set.add(int(e))
        sets.append(new_set)
        i += 1

    # processes the list so we get unions and interceptions member counts.
    first_set = sets[0]
    unions_set = first_set
    intersections_set = first_set
    for cur_set in sets[1:]:
        unions_set = unions_set.union(cur_set)
        intersections_set = intersections_set.intersection(cur_set)

    # prints out the number of member for each function.
    print(len(unions_set))
    print(len(intersections_set))
else:
    print(0)
    print(0)