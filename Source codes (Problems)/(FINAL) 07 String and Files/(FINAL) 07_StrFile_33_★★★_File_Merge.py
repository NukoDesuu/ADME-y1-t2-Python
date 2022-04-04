numArr = '0123456789. '

def StudentSort(stdl):
    sortingList = []
    for li in stdl:
        temp = []
        faculty = li[8:10]
        acadYear = li[:2]
        sid = li[2:8]
        grade = li[11:]

        temp.append(faculty)
        temp.append(acadYear)
        temp.append(sid)
        temp.append(grade)

        sortingList.append(temp)

    sortedData = sorted(sortingList)

    polishedSorted = []

    for s in sortedData:
        faculty = s[0]
        acadYear = s[1]
        sid = s[2]
        grade = s[3]

        string = acadYear + sid + faculty + " " + grade
        polishedSorted.append(string)

    return polishedSorted

def FileCombine(f1, f2):
    combined = f1 + f2
    return combined

# inp = ["E:/Nono/Programming/Sample data files/Data A.txt", "E:/Nono/Programming/Sample data files/Data B.txt"] (test case for my local pc)
inp = input().split()
file1 = str(inp[0])
file2 = str(inp[1])

#####

fileInstance1 = open(file1, "r")

line1 = fileInstance1.readline()

lines1 = []

while len(line1) > 0:
    linec1 = ''
    for c in line1:
        if c in numArr:
            linec1 += c
    lines1.append(linec1)
    line1 = fileInstance1.readline()

fileInstance1.close()

#####

fileInstance2 = open(file2, "r")

line2 = fileInstance2.readline()

lines2 = []

while len(line2) > 0:
    linec2 = ''
    for c in line2:
        if c in numArr:
            linec2 += c
    lines2.append(linec2)
    line2 = fileInstance2.readline()

fileInstance2.close()

#####

lineSum = FileCombine(lines1, lines2)
studentSort = StudentSort(lineSum)

for i in studentSort:
    print(i) 