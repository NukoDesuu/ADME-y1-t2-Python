inp = input()
scores = inp.split()

#getting values from input
a = float(scores[0])
b = float(scores[1])
c = float(scores[2])
d = float(scores[3])

#sorting algorithm for 4 items
if a > b:
	a,b = b,a
if a > c:
	a,c = c,a
if a > d:
	a,d = d,a
if b > c:
	b,c = c,b
if b > d:
	b,d = d,b
if c > d:
	c,d = d,c

#averaging 2 selected items
avg = round((b + c) / 2, 2)

#outputting results
print(avg)