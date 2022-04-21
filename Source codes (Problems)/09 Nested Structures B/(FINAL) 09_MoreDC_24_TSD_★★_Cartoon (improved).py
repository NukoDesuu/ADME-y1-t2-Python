cartoon_name_type = dict()

inp = input()
type_order = []

while inp != "q":
    comp = inp.split(", ")
    name = comp[0]
    type = comp[1]
    if type not in cartoon_name_type:
        cartoon_name_type[type] = [name]
        type_order.append(type)
    else:
        cartoon_name_type[type] += [name]
    inp = input()

for t_order in type_order:
    print(t_order + ": " + ", ".join(cartoon_name_type[t_order]))