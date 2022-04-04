def MinToTimeStr(m):
    h = m // 60
    rm = m % 60
    if rm < 10:
        zero = '0'
    else:
        zero = ''
    return str(h) + ":" + zero + str(rm)

def TimeStrToMin(t):
    comp = t.split(":")
    h = int(comp[0])
    m = int(comp[1])
    return (h * 60) + m

n = int(input())

i = 0
genre_durations = {}
while i < n:
    inp = input().split(", ")
    genre = inp[2]
    dur = TimeStrToMin(inp[3])
    if genre not in genre_durations:
        genre_durations[genre] = dur
    else:
        genre_durations[genre] += dur
    i += 1

sorting_list = []

for g,d in genre_durations.items():
    sorting_list.append([d,g])

LongestFirstDur = sorted(sorting_list, reverse=True)

if len(LongestFirstDur) >= 3:
    Top3 = LongestFirstDur[:3]
else:
    Top3 = LongestFirstDur

for e in Top3:
    top_min = e[0]
    top_genre = e[1]
    out = top_genre + " ---> " + MinToTimeStr(top_min)
    print(out)