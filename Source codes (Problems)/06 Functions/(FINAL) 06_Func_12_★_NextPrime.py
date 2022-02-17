def is_prime(n):
    #check whether if the number n is prime.
    if n <= 1:
        return False
    for k in range(2, int(n**0.5)+1):
        if n % k == 0:
            return False
    return True

def next_prime(x):
    #check for next prime number
    if is_prime(x) == True: #if the said number is already prime, you should get the NEXT one!
        x += 1
    while is_prime(x) == False:
        x += 1
    return x

def next_twin_prime(y):
    #check for the next 2 prime numbers which have difference of 2
    a = next_prime(y)
    b = next_prime(y + 2)
    while not((b - a) == 2):
        a = next_prime(y)
        b = next_prime(y + 2)
        y += 1
    out = "(" + str(a) + ", " + str(b) + ")"
    return out

#a line of code essential for the Grader system (disable this for debugging)
exec(input().strip())