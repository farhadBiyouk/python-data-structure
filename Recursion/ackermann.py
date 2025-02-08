def ack(num1, num2, s='%s'):
	print(s % ('ack (%d,%d)' % (num1, num2)))
	if num1 == 0:
		return num2 + 1
	elif num2 == 0:
		return ack(num1 - 1, 1)
	else:
		return ack(num1 - 1, ack(num1, num2 - 1, s % ('ack(%d, %%s)' % (num1  -1))),s)

print(ack(1,1))