inp = input()

length = len(inp)
check_no = inp[0:2]

check_list = ['06', '08', '09']

if length == 10 and check_no in check_list:
	print("Mobile number")
else:
	print("Not a mobile number")