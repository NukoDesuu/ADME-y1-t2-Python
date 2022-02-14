inp = input()

n = len(inp)
chars = [''] * n

nums = [n for n in '0123456789']

for i in range(n):
    chars[i] = inp[i]

exist_nums = []

for c in chars:
    if c in nums and c not in exist_nums:
        exist_nums += c

remain_nums = []

for k in nums:
    if k not in exist_nums:
        remain_nums += k

if len(remain_nums) == 0:
    out = 'None'
else:
    out = ','.join(remain_nums)

print(out)