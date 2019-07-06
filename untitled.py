#!/usr/local/lib
# -*-coding:Utf-8 -*

def afficher_flottant(beuleu):
	if type(beuleu)is not float:
		raise TypeError("le paramètre doit être un float")
	beuleu=str(beuleu)
	partie_entiere, partie_flottante=beuleu.split(".")
	beuleu2=",".join([partie_entiere,partie_flottante[:3]])
	print(beuleu2)

afficher_flottant(3.99999999)

