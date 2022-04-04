basicBases = 'ATCG'
complBases = 'TAGC'

def CheckDNA(ds):
    for b in ds:
        if b not in basicBases:
            return False
    return True

def R(ds):
    rvcs = ''
    for b in ds:
        rvcs += complBases[basicBases.index(b)]
    rvcs = rvcs[::-1]
    return rvcs

def F(ds):
    A_count,T_count,C_count,G_count = 0,0,0,0
    for b in ds:
        if b == "A":
            A_count += 1
        elif b == "T":
            T_count += 1
        elif b == "C":
            C_count += 1
        elif b == "G":
            G_count += 1
    out = "A=" + str(A_count) + ", T=" + str(T_count) + ", G=" + str(G_count) + ", C=" + str(C_count)
    return out

def D(ds):
    pair = input()
    pair_count = 0
    ini = ds[:2]
    if ini == pair:
        pair_count += 1
    for k in range(2,len(ds) - 1):
        p = ds[k] + ds[k+1]
        if p == pair:
            pair_count += 1
    return pair_count

dnaStrand = input().upper()
op = input()

command = 'RFD'
func = [R, F, D]

if CheckDNA(dnaStrand):
    out = func[command.index(op)](dnaStrand)
else:
    out = "Invalid DNA"

print(out)