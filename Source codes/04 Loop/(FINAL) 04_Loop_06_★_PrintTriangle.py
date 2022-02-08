h = int(input()) #height

b = (2*h) - 1 #base width

#mid = int((b + 1) / 2) #

canvas = ""

space = " " #space entry (no stroke)
brs = "*" #brush stroke entry (stroke)

for y in range(h):
    #print(y) #for debugging (show number of line - 1)

    if y == 0: #first line
        front = space * (h - 1)
        back = front
        print(front + brs + back)

    elif not (y == (h - 1)): #middle lines
        front = space * (h - (1 + y))
        mid = space * (2*y - 1)
        back = front
        print(front + brs + mid + brs + back)

    else: #last line
        line = brs * b
        print(line)