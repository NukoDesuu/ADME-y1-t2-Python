import codecs

with codecs.open("input.txt", encoding='utf-8', mode='r') as f:
    renamed = []
    i = 0
    for l in f:
        if i == 0:
            folder = l
            i += 1
        else:
            items = l.split()
            renamed.append(items[0] + ".py")

dataPath = 'D:\\Nono\\WORKS\\Programming\\ONLINE SYNCED SOURCES\\ADME-y1-t2-Python\\Source codes (Problems)\\' + folder[:-2]

print("Selected folder : " + folder[:-2])
print("Path : " + dataPath)

for e in renamed:
    fullPath = dataPath + '\\' + e
    open(fullPath, 'w').close()

print('\ndone')