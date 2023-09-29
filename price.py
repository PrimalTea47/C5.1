from random import randint

juste = randint(1,1000)
essais = []

while True:
	user = int(input('Enter a price >>> '))
	if user == juste:
		essais.append(user)
		print('Found in',len(essais),'trys ! : ',essais)
		break

	elif user < juste:
		essais.append(user)
		print('MORE !!!')

	elif user > juste:
		essais.append(user)
		print('LESS !!!')

	else:
		print('ERROR !!!')