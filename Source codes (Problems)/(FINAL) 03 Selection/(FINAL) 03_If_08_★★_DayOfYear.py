d = int(input())
m = int(input())
by = int(input())

#calculate for christian year
cy = by - 543

#determine if the year is a leap year or not
ld = 0
if cy % 100 == 0: #exclusive for century year (multiple of 100), leap year IS divisible by 400
    if cy % 400 == 0:
        ld = 1
elif cy % 4 == 0: #other leap years are divisible by 4
    ld = 1

#calculate for number of days in a year
td = d
#there are better ways to do this but let assume I don't know about loop in this problem yet lol
#here is through the use of cumulative sum
if m == 2:
    td += 31
if m == 3:
    td += 59
if m == 4:
    td += 90
if m == 5:
    td += 120
if m == 6:
    td += 151
if m == 7:
    td += 181
if m == 8:
    td += 212
if m == 9:
    td += 243
if m == 10:
    td += 273
if m == 11:
    td += 304
if m == 12:
    td += 334

if m > 2: #leap day will guarantee to be taken in account after 29 feb
    td += ld
#output
print(td)