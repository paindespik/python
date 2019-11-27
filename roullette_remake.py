#!/usr/local/lib
# -*-coding:Utf-8 -*
import random
bourse=0

while bourse<=0 :
    try:
        bourse=int(input("De quelle somme d'agent disposez-vous?"))
        assert bourse>0
    except ValueError :
        print("Vous devez rentrer un nombre")
    except AssertionError :
        print("Vous devez rentrer un nombre supérieur à 0")
continuer="o"
while bourse > 0 and continuer == "o":
    numero = -1
    while numero<=0 or numero >49:
        try:
            numero=int(input("Sur quel numéro voulez-vous miser ?"))
            assert numero>=0 and numero <=49
        except ValueError:
            print("Vous devez rentrer un nombre")
        except AssertionError :
            print("Vous devez rentrer un nombre entre 0 et 49")
    mise = 0
    while mise<=0 or mise>bourse:
        try:
            mise=int(input("Combien souhaitez-vous miser?"))
            assert mise >0 and mise <= bourse
        except ValueError :
            print("Vous devez rentrer un nombre")
        except AssertionError :
            print ("Vous devez rentrer un nombre supérieur à 0 et inférieur à votre argent total")
    rand=random.randint(0,50)
    if numero==rand :
        print("BRAVO!!!!! Vous etes tombé sur le numero gagnant : ", rand)
        bourse+=mise*2
    elif numero%2==rand%2 :
        print ("Vous etes tombé sur le numéro ", rand)
        print("Vous n'etes pas tombé sur le bon numéro mais vous avez la bonne couleur. Vous conservé votre mise")
    else :
        print ("Vous etes tombé sur le numéro ", rand)
        print("Vous perdez votre mise")
        bourse-=mise
    print("Vous avez ", bourse, "euros")

    continuer=input("souhaitez vous continuer ? (rentrer o pour oui ou n pour non)")





