def month_num(n):
    mname = ["Jan", "Feb", "Mar", "Apr", 
             "May", "Jun", "Jul", "Aug",
             "Sep", "Oct", "Nov", "Dec"]
    num = mname.index(n) + 1
    return num

def read_date():
    date = input().split()
    d = date[0]
    m = month_num(date[1])
    y = date[2]
    return [int(d),int(m),int(y)]

def zodiac(d,m):
    monA = ["Aries", "Taurus", "Gemini", "Cancer",
            "Leo", "Virgo", "Libra", "Scorpio",
            "Sagitarrius"]
    if (m == 3 and d > 21) or (m == 12 and d < 22) or (4 <= m <= 11):
        mon = m - 3
        if d <= 21:
            mon -= 1
        return monA[mon]
    else:
        if (m == 12) or (m == 1 and d <= 20):
            return "Capricorn"
        elif (m == 1 and d >= 1) or (m == 2 and d <= 20):
            return "Aquarius"
        else:
            return "Pisces"

def days_in_feb(y):
    if (y % 400 == 0) or ((y % 100 != 0) and (y % 4 == 0)):
        return 29
    return 28

def days_in_month(m,y):
    if m in [4,6,9,11]:
        return 30
    elif m == 2:
        return days_in_feb(y)
    return 31

def days_in_between(d1,m1,y1,d2,m2,y2):
    sy = y1
    m_day = [31, days_in_feb(sy), 31, 30,
             31, 30, 31, 31,
             30, 31, 30, 31]
    dm1,dm2 = 0,0
    for i in range(m1,12):
        dm1 += m_day[i]
    sy = y2
    for j in range(m2-1):
        dm2 += m_day[j]
    totdif = dm1 + dm2 + (days_in_month(m1,y1) - d1 + 1) + int((y2 - y1 - 1)*365.25) + (d2 - 1)
    return totdif

def main():
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))

main()