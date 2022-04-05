def knows(R, x, y):
    if y in R[x]:
        return True
    return False

def is_celeb(R, x):
    if x in R:
        if len(R[x]) != 0 and not(x in R[x]):
            return False
        elif len(R[x]) == 1 and x in R[x] and len(R) == 1:
            return True
    for beingKnown in R.values():
        if x not in beingKnown:
            return False
    return True

def find_celeb(R):
    sample = set()
    for whoKnows, isKnown in R.items():
        if whoKnows not in sample:
            sample.add(whoKnows)
        sample = sample.union(isKnown)
    for s in sample:
        if is_celeb(R, s):
            return s
    return None

def read_relations():
    R = dict()
    inp = input()
    while inp != "q":
        comp = inp.split()
        a = comp[0]
        b = comp[1]
        if a not in R:
            R[a] = set()
            R[a].add(b)
        else:
            R[a].add(b)
        inp = input()
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None:
        print("Not Found")
    else:
        print(c)

exec("print(find_celeb({'D':{'Z'},'Q':{'Z'},'C':{'B','Z'},'B':{'Q','Z'},'Z':set()}))")