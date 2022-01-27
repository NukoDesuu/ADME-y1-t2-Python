#INPUT

# check the flowchart and be sure to use specifically this code to receive inputs for this problem!
d,m,y = [int(e) for e in input().split()]

#PROCESS

# the given year is "Bhuddhist year" so it has to be converted into "Century year" first
cy = y - 543

n = 31 # days in most of the months

# defining (elements containing) months with 30 days by number
# April (4), June (6), September (9), November (11)
_30daysM = [4, 6, 9, 11]

if m in _30daysM :
    n = 30
elif m == 2 :
    n = 28
    if ( (cy % 400) == 0 ) or ( ( (cy % 4) == 0 ) and not( (cy % 100) == 0 ) ) :
        n = 29
else :
    pass

td = d + 15

if td > n : # shifting a month
    td = td - n
    m = m + 1

if m > 12 : #shifting a year
    m = m - 12
    y = y + 1

#variables to be printed : td , m , y
td = str(td)
m = str(m)
y = str(y)

#OUTPUT
print(td + "/" + m + "/" + y)