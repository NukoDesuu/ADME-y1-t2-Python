def SpaceElementRemove(l):
    nonEmpty = []
    for e in l:
        if e != ' ':
            nonEmpty.append(e)
    return nonEmpty

line1 = SpaceElementRemove(sorted(input().lower()))
line2 = SpaceElementRemove(sorted(input().lower()))

anag = "YES"

if len(line1) != len(line2) or line1 != line2:
    anag = "NO"

print(anag)