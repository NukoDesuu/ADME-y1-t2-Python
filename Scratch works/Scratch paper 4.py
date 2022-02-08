inp = float(input())
min_v = inp
while not(inp == 'q'):
    inp = float(input())
    if inp < min_v:
        min_v = inp

print(min_v)
    