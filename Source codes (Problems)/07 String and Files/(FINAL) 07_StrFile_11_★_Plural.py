word = input()

# checkLetter1 and 2 are located from the left most and the following character accordingly

checkLetter1 = word[-1]
checkLetter2 = word[-2]

if checkLetter1 in "sx" or (checkLetter1 == 'h' and checkLetter2 == 'c'):
    out = word + 'es'
elif (checkLetter1 == 'y' and checkLetter2 not in 'aeiou'):
    withoutY = word[:len(word) - 1]
    out = withoutY + 'ies'
else:
    out = word + 's'

print(out)
