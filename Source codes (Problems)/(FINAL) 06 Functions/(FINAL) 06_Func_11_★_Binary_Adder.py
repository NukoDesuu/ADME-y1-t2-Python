bi_nums = input().split()

bi_x = bi_nums[0]
bi_y = bi_nums[1]

b10_x = int(bi_x, 2)
b10_y = int(bi_y, 2)

b_10_sum = b10_x + b10_y
b_2_sum = bin(b_10_sum)

out = b_2_sum[2:]
print(out)