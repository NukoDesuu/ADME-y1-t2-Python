alpha_array = "abcdefghijklmnopqrstuvwxyz"

inp = input().lower()
counts = {}

for c in inp:
    if c in alpha_array:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

freqSorted = []

for k,v in counts.items():
    freqSorted.append([v,k])

freqSorted = sorted(freqSorted, reverse=True)

print(freqSorted)

alphaSorted = []
sameFreqAlpha = []
totalSorted = []
ie = 0
rep = 0
repc = 0
n = 0
max_n = len(freqSorted)

for e in freqSorted:
    f = e[0]
    a = e[1]
    if ie == 0:
        inif = f
        inia = a
        ie = 1
    elif f == inif:
        if rep == 0:
            sameFreqAlpha.append([inif, inia])
        sameFreqAlpha.append([f, a])
        rep = 1
    else:
        if rep == 1:
            for s in sorted(sameFreqAlpha):
                totalSorted.append(s)
        else:
            totalSorted.append([inif, inia])
        inif = f
        inia = a
        sameFreqAlpha = []
        rep = 0
    
    n += 1

    if n == max_n:
        if rep == 1:
            for r in sorted(sameFreqAlpha):
                totalSorted.append(r)
        else:
            totalSorted.append([f, a])

print(totalSorted)

for pair in totalSorted:
    f = pair[0]
    a = pair[1]
    print(a + " -> " + str(f))