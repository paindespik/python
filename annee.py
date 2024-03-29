#!/usr/local/lib
# -*-coding:Utf-8 -*
# Programme testant si une année, saisie par l'utilisateur, est bissextile ou non

annee = input("Saisissez une année : ") # On attend que l'utilisateur fournisse l'année qu'il désire tester
try:
	annee = int(annee) # Risque d'erreur si l'utilisateur n'a pas saisi un nombre
	if annee<=0:
		raise inf ("votre année doit être supérieur à zéro")
except ValueError:
	print("erreur: il faut rentrer un entier")
except inf:
	print("veuillez rentrer une année supérieur 0")

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
    print("L'année saisie est bissextile.")
else:
    print("L'année saisie n'est pas bissextile.")