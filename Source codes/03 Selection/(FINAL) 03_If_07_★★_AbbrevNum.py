n = int(input())

b = int('1' + ('0' * 9))
m = int('1' + ('0' * 6))
k = int('1' + ('0' * 3))

bu = n // b
mu = n // m
ku = n // k

dout = 0
lv = ''

if bu == 0:
	if mu == 0:
		if ku == 0:
			uout = n
		else:
			lv = "K"
			if ku < 10:
				rku = n % k
				dout = round(rku / k, 1) % 1
			else:
				if (n % k) >= (5 * (k / 10)):
					ku += 1
			uout = ku
	else:
		lv = "M"
		if mu < 10:
			rmu = n % m
			dout = round(rmu / m, 1) % 1
		else:
			if (n % m) >= (5 * (m / 10)):
				mu += 1
		uout = mu
else:
	lv = "B"
	if bu < 10:
		rbu = n % b
		dout = round(rbu / b, 1) % 1
	else:
		if (n % b) >= (5 * (b / 10)):
			bu += 1
	uout = bu

###outputting zone

print(str(uout + dout) + lv)