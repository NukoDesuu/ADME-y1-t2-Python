cartoon_name_type = dict()

inp = input()

while inp != "q":
    comp = inp.split(", ")
    name = comp[0]
    type = comp[1]
    if type not in cartoon_name_type:
        cartoon_name_type[type] = [name]
    else:
        cartoon_name_type[type] += [name]
    inp = input()

for t,nl in cartoon_name_type.items():
    print(t + ": " + ", ".join(nl))