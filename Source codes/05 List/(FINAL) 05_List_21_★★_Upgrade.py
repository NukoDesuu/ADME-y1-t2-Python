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

result = []

for n in range(len(ids)):
    result.append(ids[n] + " " + grades[n])

out = sorted(result)

for l in out:
    print(l)