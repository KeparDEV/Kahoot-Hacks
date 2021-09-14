import os
import sys
from time import sleep
from PIL import Image


os.system('')
os.system('cls')

path1 = os.getcwd()
Kflooder_check = os.path.isfile(path1 + '/Kahoot/Kahot-flooder/flooder.js')	

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

choice = 4

words = bcolors.OKGREEN + """

	 ██ ▄█▀▓█████  ██▓███   ▄▄▄       ██▀███  
	 ██▄█▒ ▓█   ▀ ▓██░  ██▒▒████▄    ▓██ ▒ ██▒
	▓███▄░ ▒███   ▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒
	▓██ █▄ ▒▓█  ▄ ▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄  
	▒██▒ █▄░▒████▒▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒
	▒ ▒▒ ▓▒░░ ▒░ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░
	░ ░▒ ▒░ ░ ░  ░░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░
	░ ░░ ░    ░   ░░         ░   ▒     ░░   ░ 
	░  ░      ░  ░               ░  ░   ░     
                                          

                    
     		\033[91mKahoot Hack"""

for char in words:
	sleep(0.005)
	sys.stdout.write(char)
	sys.stdout.flush()

while True :
	os.system('cls')
	print(bcolors.OKGREEN + '')
	print(words)
	print(bcolors.OKCYAN + """

		1) Kahoot Answer hack

		2) Kahoot Flooder


		3) quit

		""")



	choice = input('               choice: ')

	if choice == '1':
		Sec_path = path1 + '\\Kahoot\\kahoot-answer-bot'
		print('')

		os.system('py -3 -m pip install -r "' + Sec_path + '\\requirements.txt"')

		sleep(3)

		os.system('cls')\
		

		print('Name = Name of the Auto Answer BOT')
		print('Pin = Game Pin e.g.: 123 4567')
		print('QuizID = (look the image witch just poped)')
		print('')

		sleep(2)

		im = Image.open(path1 + "\Kahoot\quizid.png") 
		im.show()

		sleep(3)


		os.system('py -3 "' + Sec_path + '\\kbot"')
		break


	if choice == '2':
		
		os.system('cls')
		print('Make Sure Node.js is installed')
		os.system('pause')

		path = path1 + '\\Kahoot\\Kahoot-flooder'

		check1 = os.path.isfile('flood.js')

		if check1 == True :
			os.remove('flood.js')

		os.chdir(path)

		os.system('cls')

		pin = int(input('Game Pin:  '))

		os.system('cls')

		name = input('Bots Name:   ')

		os.system('cls')

		amount = int(input('Amount of bots, (suggestion: (1-60)):   '))




		f = open("flood.js", "w")
		f.write("const KahootSpam = require('kahoot-spam') \n")
		f.write("let api = KahootSpam \n")
		f.write('api.spamWithAnswers(' + str(pin) + ', \"' + name + '\", ' + str(amount) + ', true)')
		f.close()

		os.system('npm install kahoot-spam')
		os.system('node flooder.js')
		os.system('pause')
		break

	if choice == '3':
		os.system('cls')
		exit()






os.system("cls")
print(words)
print("""

	Thanks for Using the Kepar Kahoot Hack

	""")

	
sleep(3)
os.system('start https://www.youtube.com/channel/UCJ2l3NRmNrmtOkcMjXycbcg')

exit()

