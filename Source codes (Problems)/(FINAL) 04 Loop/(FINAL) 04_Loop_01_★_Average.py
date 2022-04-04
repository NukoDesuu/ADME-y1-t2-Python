inp = input()

n = 0
tot = 0

while inp != "q":
    n += 1
    tot += float(inp)
    inp = input()

if n == 0:
    print("No Data")
else:
    avg = round(tot / n, 2)
    print(avg)