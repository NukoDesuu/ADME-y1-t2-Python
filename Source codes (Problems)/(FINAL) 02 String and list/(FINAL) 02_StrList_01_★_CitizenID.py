ID = input()

a = int((ID[0])) * 13
b = int((ID[1])) * 12
c = int((ID[2])) * 11
d = int((ID[3])) * 10
e = int((ID[4])) * 9
f = int((ID[5])) * 8
g = int((ID[6])) * 7
h = int((ID[7])) * 6
i = int((ID[8])) * 5
j = int((ID[9])) * 4
k = int((ID[10])) * 3
l = int((ID[11])) * 2

check_id = (11 - ((a+b+c+d+e+f+g+h+i+j+k+l) % 11)) % 10

g1 = ID[0]
g2 = ID[1] + ID[2] + ID[3] + ID[4]
g3 = ID[5] + ID[6] + ID[7] + ID[8] + ID[9]
g4 = ID[10] + ID[11]
g5 = check_id

print(str(g1) + " " + str(g2) + " " + str(g3) + " " + str(g4) + " " + str(g5))