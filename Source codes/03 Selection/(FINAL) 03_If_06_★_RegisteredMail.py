w = int(input())

if w <= 100:
	c = '18'
elif 100 < w <= 250:
	c = '22'
elif 250 < w <= 500:
	c = '28'
elif 500 < w <= 1000:
	c = '38'
elif 1000 < w <= 2000:
	c = '58'
else:
	c = 'Reject'
	
print(c)