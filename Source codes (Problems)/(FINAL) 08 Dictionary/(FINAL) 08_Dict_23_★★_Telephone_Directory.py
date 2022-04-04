def reverse(d):
    reversed_dict = {}
    for k,v in d.items():
        reversed_dict[v] = k
    return reversed_dict

n = int(input())

i = 0
name_list = {}

while i < n:
    entry = input().split()
    full_name = " ".join(entry[:2])
    tel = entry[2]
    name_list[full_name] = tel
    i += 1

m = int(input())

j = 0
query_list = []

while j < m:
    query_list.append(input())
    j += 1

tel_list = reverse(name_list)

output_list = []

for q in query_list:
    if q in name_list:
        output_list.append(name_list[q])
    elif q in tel_list:
        output_list.append(tel_list[q])
    else:
        output_list.append("Not found")

num = len(query_list)
for k in range(num):
    print(query_list[k] + " --> " + output_list[k])