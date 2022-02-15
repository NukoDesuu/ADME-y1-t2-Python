n = int(input())

pair = [""] * n
x_list = [""] * n
y_list = [""] * n
red = [""] * n
blue = [""] * n

for i in range(n):
    pair[i] = input()

e = 0

for p in pair:
    x_list[e] = int((p.split())[0])
    y_list[e] = int((p.split())[1])
    e += 1

type = input()

m = 0

while m < n:
    if type == "Zig-Zag":
        red[m] = x_list[m]
        blue[m] = y_list[m]
        m += 1
        if m < n:
            red[m] = y_list[m]
            blue[m] = x_list[m]
            m += 1
    else:
        blue[m] = x_list[m]
        red[m] = y_list[m]
        m += 1
        if m < n:
            blue[m] = y_list[m]
            red[m] = x_list[m]
            m += 1

min_value = min(red)
max_value = max(blue)

print(str(min_value) + " " + str(max_value))