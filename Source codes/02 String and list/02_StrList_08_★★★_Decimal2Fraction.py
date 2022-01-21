from socket import AF_DECnet


dcm_num = input()

comp = dcm_num.split(",")

before = comp[0]
after = comp[1]
repeat = comp[2]

print(before)
print(after)
print(repeat)