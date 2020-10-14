def botts(num):
	if num == 0:
		return 'No bottles '
	if num == 1:
		return '1 bottle '
	return str(num) + ' bottles '

def bottles(num, orig = -1):
	if num < 0:
		return
	if num > orig:
		orig = num
	print(botts(num) + 'of beer on the wall, ' + botts(num) + 'of beer!')
	if num == 0:
		print('Go to the store and buy some more...')
		print(botts(orig) + 'of beer on the wall!')
	if num > 0:
		print('Take one down and pass it around...')
		print(botts(num-1) + 'of beer on the wall!\n')
	bottles(num-1, orig)
