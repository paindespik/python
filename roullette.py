#!/usr/local/lib
# -*-coding:Utf-8 -*
import random
sommeArgent =input("quel est votre somme d'argent de départ:  ")
numeroMise=0
mise=0
try:
	sommeArgent=int(sommeArgent)
	assert sommeArgent>0
except  ValueError:
	print("vous devez rentrer un nombre")
except AssertionError:
	print("vous devez rentrer une somme d'argent supérieur à 0")

while sommeArgent>0:
	numeroMise=input("Sur quel nupéro souhaiter vous miser? (entre 0 et 49)")
	try:
		numeroMise=int(numeroMise)
		assert numeroMise>=0 
		assert numeroMise<=49
	except:
		print("vous devez rentrer un nombre compris entre 0 et 49")
	mise=input("Combien d'argent souhaiter vous miser?")
	try:
		mise=int(mise)
		assert mise<=sommeArgent
		assert mise>0
	except :
		print("vous devez rentrer un numéro")
	rand=random.randint(0,50)
	if rand==numeroMise:
		print("BRAVO!!! vous êtes tombé sur votre numéro! Vous gagnez ",mise*3, "euros")
		sommeArgent+=mise*3

	elif random.randint(0,2)==0:
		print("vous etes tombés sur le numéro", rand)
		print("vous n'êtes pas tombé sur le bon numéro, mais vous gardé la moitié de votre mise, car vous être tombé sur la bonne couleur")	
		sommeArgent-=mise/2
	else:
		print("vous etes tombé sur le numéro", rand)
		print("pas de chance, vous perdez votre mise")
		sommeArgent-=mise
	print("il vous reste", sommeArgent, "euros")


