driving = input('請問你有沒有開過車?(Y/N)')
if driving !='Y' and driving !='N':
	print('只能輸入Y/N')
	raise systemexit

age = input('請輸入你的年齡:')
age = int(age)
if driving == 'Y':
	if age >=18:
		print('Congratulation you pass!')
	else:
		print('why do not you never driving?')	
elif driving == 'N':
	if age >=18:
		print('you can driving go ahead!')
	else:
		print('nice guy!')



