import codecs #helps reading special characters from files
import pyperclip as p #enables clipboard copying and pasting (copy(), paste())

def removeP(o, t):
    rng = len(t) - 2
    return o[rng-1:]

with codecs.open("input.txt", encoding='utf-8', mode='r') as f:
    renamed = []
    i = 0
    for l in f:
        if i == 0:
            folder = l
            i += 1
        else:
            items = l.split()
            renamed.append(items[0] + removeP(items[1], items[0]) + ".py")

dataPath = 'E:\\Nono\\Programming\\ONLINE SYNCED SOURCES\\ADME-y1-t2-Python\\Source codes (Problems)\\' + folder[:-2]

print("Selected folder : " + folder[:-2])
print("Path : " + dataPath)

for e in renamed:
    fullPath = dataPath + '\\' + e
    open(fullPath, 'w').close()

print('\ndone')