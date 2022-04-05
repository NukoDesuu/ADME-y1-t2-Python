n = int(input())

i = 0
database = []
while i < n:
    comps = input().split()
    database.append(comps)
    i += 1

targets = input().split()
result = []

for student in database:
    void = 0
    for t in targets:
        if t not in student or t == student[0]:
            void += 1
    if void == 0:
        result.append(student)

for out in sorted(result):
    print(" ".join(out))