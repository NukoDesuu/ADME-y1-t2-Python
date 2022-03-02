# inp = input().split()

# fileName = inp[0]
# acadYear = inp[1]

dataLines = []

file = open("E:/Nono/Programming/Sample data files/Data A.txt" , "r")

line = file.readline()

while len(line) > 0:
    dataLines.append(line[:-1])
    line = file.readline()

file.close()

print(dataLines)