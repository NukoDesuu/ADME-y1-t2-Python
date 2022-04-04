n = int(input())

set1 = []
set2 = []
set3 = []

if n != 0:
    set1 = [int(input()) for i in range(n)]

term = input()

if term != '-1':
    set2 = [int(n) for n in term.split()]
    
    term = int(input())
    
    while term != -1:
        set3.append(int(term))
        term = int(input())

pool = set1 + set2 + set3

ini = 0

if len(pool) % 2 == 1:
    ini = -2
else:
    ini = -1

back = pool[ini::-2]
fwd = pool[0::2]

out = back + fwd
print(out)