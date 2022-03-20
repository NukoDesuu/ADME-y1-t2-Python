def reverse(d):
    reversed_dict = {}
    for k,v in d.items():
        reversed_dict[v] = k
    return reversed_dict

n = int(input())

i = 0
full_nicks = {}

while i < n:
    inp = input().split()
    full = inp[0]
    nick = inp[1]
    full_nicks[full] = nick
    i += 1

m = int(input())

j = 0
target_names = []

while j < m:
    target_names.append(input())
    j += 1

matches = []
nick_fulls = reverse(full_nicks)

for name in target_names:
    if name in full_nicks:
        matches.append(full_nicks[name])
    elif name in nick_fulls:
        matches.append(nick_fulls[name])
    else:
        matches.append("Not found")

for out in matches:
    print(out)