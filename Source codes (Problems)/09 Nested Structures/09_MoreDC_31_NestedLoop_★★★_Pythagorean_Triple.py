def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def is_coprime(a, b, c):
    if gcd(a, b) == 1 or gcd(b, c) == 1 or gcd(a, c) == 1:
        return True
    return False

def primitive_Pythagorean_triples(max_len):
    triple = []
    doublePrimes = [] #using doublePrimes pairs for faster speed
    for a in range(1, max_len):
        for b in range(a+1, max_len):
            if gcd(a, b) == 1:
                doublePrimes.append([a,b])
    for pairs in doublePrimes:
        e1, e2 = pairs[0], pairs[1]
        for c in range(e2, max_len):
            if is_coprime(e1, e2, c) and (e1**2 + e2**2 == c**2):
                triple.append([e1, e2, c])
    
    def a_c_swap(L):
        swapped = []
        for list in L:
            swapped.append([list[2], list[1], list[0]])
        return swapped
    
    sorting_triple = a_c_swap(triple)
    print(sorting_triple)
    sorted_triple = sorted(sorting_triple)
    print(sorted_triple)
    final_triple = a_c_swap(sorted_triple)

    return final_triple

print(primitive_Pythagorean_triples(100)[-10:])