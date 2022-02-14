nums = [int(n) for n in input().split()]

nums.sort()

u_count = 0
u_list = []
ini = None

for a in nums:
    if ini == None:
        ini = a
        u_list.append(a)
        u_count += 1
    else:
        if a != ini:
            u_count += 1
            if len(u_list) < 10:
                u_list.append(a)
            ini = a       

print(u_count)
print(u_list)