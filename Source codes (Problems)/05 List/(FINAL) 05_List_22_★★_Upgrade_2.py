gradings = ['F', 'D', 'D+', 'C', 'C+', 'B', 'B+', 'A']

ids = []
grades = []

inps = input()

while inps != 'q':
    ids.append(inps.split()[0])
    grades.append(inps.split()[1])
    inps = input()

up_ids = input().split()

for i in up_ids:
    if i in ids:
        who = ids.index(i)
        g = gradings.index(grades[who])
        if g != 7:
            g += 1
            grades[who] = gradings[g]

for n in range(len(ids)):
    print(ids[n] + " " + grades[n])