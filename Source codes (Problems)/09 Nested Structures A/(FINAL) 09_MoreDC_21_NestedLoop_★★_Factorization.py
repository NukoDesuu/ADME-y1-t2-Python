def factor(N):
    k = 2
    naives = []
    while not(k > N):
        divisible = True
        times = 0
        while divisible == True:
            if N % k == 0:
                N //= k
                times += 1
            else:
                divisible = False
        if times != 0:
            naives.append([k,times])
        k += 1
    return naives

exec(input().strip())