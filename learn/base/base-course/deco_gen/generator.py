def grep(str):
	print('start')
	k = 0
	while True:
		value = yield k
		k += 1
		print('.........', value)

c = grep()
