lowerAlphaArr = 'abcdefghijklmnopqrstuvwxyz'
upperAlphaArr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numArr = '0123456789'
nonSymbol = lowerAlphaArr + upperAlphaArr + numArr

Specials = '!@#$%^&*()_+'

keyboardRowA = []

for c in Specials:
    keyboardRowA.append(c)

keyboardRowB = 'qwertyuiop'
keyboardRowC = 'asdfghjkl'
keyboardRowD = 'zxcvbnm'

def EnoughLength(s):
    if len(s) >= 8:
        return True
    return False

def UniqueLetters(s):
    le,ue,ne,se = 0,0,0,0
    lacks = []
    for c in s:
        if c in lowerAlphaArr and le == 0:
            le = 1
        if c in upperAlphaArr and ue == 0:
            ue = 1
        if c in numArr and ne == 0:
            ne = 1
        if c not in nonSymbol and se == 0:
            se = 1
    if le == 0:
        lacks.append("No lowercase letters")
    if ue == 0:
        lacks.append("No uppercase letters")
    if ne == 0:
        lacks.append("No numbers")
    if se == 0:
        lacks.append("No symbols")
    
    err = len(lacks)
    
    return lacks,err

def ConsecutiveChar(s):
    rep = 0
    ini = s[0]
    for k in range(1,len(s)):
        nextl = s[k]
        if ini == nextl:
            rep += 1
            if rep == 3:
                return True
        else:
            ini = nextl
    return False

def NumberSequenceError(s):
    ne,err,fw,ner = 0,0,0,0
    for c in s:
        if c in numArr:
            n = int(c)
            if ne == 0:
                ini = n
                ne = 1
            elif abs(ini - n) == 1 or (ini == 9 and n == 0) or (ini == 0 and n == 9):
                if ner == 0:
                    if (n > ini and not(n == 9 and ini == 0)) or (n == 0 and ini == 9):
                        fw = 1
                    ner = 1
                    err += 1
                    ini = n
                elif (ner == 1) and (fw == 1):
                    if n > ini or (n == 0 and ini == 9):
                        err += 1
                        ini = n
                    else:
                        err,ne,fw = 0,0,0
                elif (ner == 1) and (fw == 0):
                    if n < ini or (n == 9 and ini == 0):
                        err += 1
                        ini = n
                    else:
                        err,ne,fw = 0,0,0
            else:
                err,ne,fw = 0,0,0
            if err == 3:
                return True
        else:
            err,ne,fw = 0,0,0
    return False

def LetterSequenceError(s):
    le,err,fw,ler = 0,0,0,0
    for c in s:
        if c not in numArr and c in nonSymbol:
            l = c.lower()
            if le == 0:
                ini = l
                le = 1
            elif abs(lowerAlphaArr.index(ini) - lowerAlphaArr.index(l)) == 1 or (ini == 'z' and l == 'a') or (ini == 'a' and l == 'z'):
                ini_index = lowerAlphaArr.index(ini)
                l_index = lowerAlphaArr.index(l)
                if ler == 0:
                    if l_index > ini_index:
                        fw = 1
                    ler = 1
                    err += 1
                    ini = l
                elif (ler == 1) and (fw == 1):
                    if l_index > ini_index or (l == 'a' and ini == 'z'):
                        err += 1
                        ini = l
                    else:
                        err,le,fw = 0,0,0
                elif (ler == 1) and (fw == 0):
                    if l_index < ini_index or (l == 'z' and ini == 'a'):
                        err += 1
                        ini = l
                    else:
                        err,le,fw = 0,0,0
            else:
                err,le,fw = 0,0,0
            if err == 3:
                return True
        else:
            err,le,fw = 0,0,0
    return False

def RowSequenceError(s):
    
    def KeyBoardRow(i):
        if i in keyboardRowA:
            rowi = 0
        elif i in keyboardRowB:
            rowi = 1
        elif i in keyboardRowC:
            rowi = 2
        elif i in keyboardRowD:
            rowi = 3
        return rowi
    
    re,err,fw,rer = 0,0,0,0
    kbr = [keyboardRowA, keyboardRowB, keyboardRowC, keyboardRowD]
    
    for c in s:
        if c not in numArr and (c in lowerAlphaArr or c in upperAlphaArr or c in keyboardRowA):
            if c not in keyboardRowA:
                c = c.lower()
            if re == 0 or (c in keyboardRowA and ini not in keyboardRowA):
                ini = c
                re = 1
            elif KeyBoardRow(c) == KeyBoardRow(ini):
                if abs(kbr[KeyBoardRow(c)].index(c) - kbr[KeyBoardRow(ini)].index(ini)) == 1:
                    ini_index = kbr[KeyBoardRow(ini)].index(ini)
                    r_index = kbr[KeyBoardRow(c)].index(c)
                    if rer == 0:
                        if r_index > ini_index:
                            fw = 1
                        rer = 1
                        err += 1
                        ini = c
                    elif (rer == 1) and (fw == 1):
                        if r_index > ini_index:
                            err += 1
                            ini = c
                        else:
                            err,fw = 0,0
                    elif (rer == 1) and (fw == 0):
                        if r_index < ini_index:
                            err += 1
                            ini = c
                        else:
                            err,fw = 0,0
                            ini = c
                else:
                    err,fw = 0,0
                    ini = c
                if err == 3:
                    return True
            else:
                err,fw = 0,0
                ini = c
        else:
            err,fw = 0,0
            if c in numArr:
                re = 0
    return False

pw = input()

ErrSuggest = []

if not(EnoughLength(pw)):
    ErrSuggest.append("Less than 8 characters")
    
err,n = UniqueLetters(pw)

if n != 0:
    for k in range(n):
        ErrSuggest.append(err[k])

if ConsecutiveChar(pw):
    ErrSuggest.append("Character repetition")

if NumberSequenceError(pw):
    ErrSuggest.append("Number sequence")

if LetterSequenceError(pw):
    ErrSuggest.append("Letter sequence")

if RowSequenceError(pw):
    ErrSuggest.append("Keyboard pattern")

en = len(ErrSuggest)

if en != 0:
    for j in range(en):
        print(ErrSuggest[j])
else:
    print("OK")