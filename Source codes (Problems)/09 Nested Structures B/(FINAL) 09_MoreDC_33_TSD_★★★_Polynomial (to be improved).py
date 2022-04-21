def add_poly(p1,p2):
    polynomial1 = dict()
    for tp in p1:
        coeff = tp[0]
        power = tp[1]
        polynomial1[power] = coeff
    
    polynomial2 = dict()
    for tp in p2:
        coeff = tp[0]
        power = tp[1]
        polynomial2[power] = coeff
    
    for p,c in polynomial2.items():
        if p not in polynomial1:
            polynomial1[p] = c
        else:
            polynomial1[p] += c
    
    out = []
    zero_coeff = []
    for p,c in polynomial1.items():
        if c == 0:
            zero_coeff.append(p)
    for z in zero_coeff:
        polynomial1.pop(z)
    
    for p,c in polynomial1.items():
        out.append(tuple([c,p]))
    
    return out

def mult_poly(p1,p2):
    polynomial1 = dict()
    for tp in p1:
        coeff = tp[0]
        power = tp[1]
        polynomial1[power] = coeff
    
    polynomial2 = dict()
    for tp in p2:
        coeff = tp[0]
        power = tp[1]
        polynomial2[power] = coeff
    
    summations = []
    for pow2,cof2 in polynomial2.items():
        for pow1,cof1 in polynomial1.items():
            cof_product = cof1 * cof2
            pow_sum = pow1 + pow2
            summations.append([cof_product, pow_sum])
    
    result = {}
    for s in summations:
        c = s[0]
        p = s[1]
        if p not in result:
            result[p] = c
        else:
            result[p] += c
    
    zero_coeff = []
    for rp,rc in result.items():
        if rc == 0:
            zero_coeff.append(rp)
    
    for z in zero_coeff:
        result.pop(z)

    out = []
    for rp,rc in result.items():
        out.append(tuple([rc,rp]))
    
    return out

p1 = [(3,6),(2,4),(1,1),(-1,0)]
p2 = []
print(add_poly(p1, p2),add_poly(p2,p1))

# for i in range(3):
#     exec(input().strip())