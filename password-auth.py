import pyttsx3

mesin = pyttsx3.init()

name= input("what is ur name? ")
password= input('how about ur password? ')

if name == 'nisa' and password == 'swordfish':
	mesin.say('Hello, Nisa, Your Access Granted')
else:
	fail= 'try again ', name
	mesin.say(fail)
mesin.runAndWait()
