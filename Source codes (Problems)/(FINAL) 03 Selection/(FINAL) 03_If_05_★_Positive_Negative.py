n = int(input())

dire = 'zero'
bit = 'even'

if n % 2 == 1:
	bit = 'odd'
	
if n > 0:
	dire = 'positive'
elif n < 0:
	dire = 'negative'
	
print(dire)
print(bit)