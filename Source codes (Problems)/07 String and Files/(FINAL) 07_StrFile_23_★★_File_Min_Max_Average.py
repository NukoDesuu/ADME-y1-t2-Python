inp = input().split()

fileName = inp[0]
acadYear = inp[1][2:]

dataLines = []

file = open(fileName , "r")

line = file.readline()

while len(line) > 0:
    dataLines.append(line[:-1])
    line = file.readline()

file.close()

inYearLines = []
    
for l in dataLines:
    if acadYear == l[:2]:
        inYearLines.append(l)

if len(inYearLines) == 0:
    out = "No data"
else:
    scores = []

    for s in inYearLines:
        e = s.split()
        scores.append(float(e[1]))

    min_score = min(scores)
    max_score = max(scores)
    mean_score = sum(scores) / len(scores)

    out = str(min_score) + " " + str(max_score) + " " + str(mean_score)

print(out)