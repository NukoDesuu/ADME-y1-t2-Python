plots = [float(n) for n in input().split()]

back = 0
mid = 0
front = 0
peak = 0

for i in range(len(plots) - 2):
    back = plots[i]
    mid = plots[i+1]
    front = plots[i+2]

    if mid > back and mid > front:
        peak += 1

print(peak)