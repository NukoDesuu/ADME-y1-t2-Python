deck = input().split()
op_in = input()
op = ""
mid = len(deck) // 2

for c in op_in:
    if c != " ":
        op += c

for o in op:
    if o in "CS":
        # SETUP per loop
        top = deck[0:mid]
        bottom = deck[mid:]
    
        #CUT method
        if o == "C":
            deck = bottom + top
    
        #SHUFFLE method
        if o == "S":
            new_deck = []
            for p in range(mid):
                new_deck.append(top[p])
                new_deck.append(bottom[p])
            deck = new_deck

out = ' '.join(deck)
print(out)