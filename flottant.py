#!/usr/local/lib
# -*-coding:Utf-8 -*


def afficherFlottant(flottant):
    if type(flottant) is not float:
        raise TypeError("Ce n'est pas un flottant")
    flottant = str(flottant)
    partieEntiere, partieFlottante = flottant.split(".")
    flottant = ",".join([partieEntiere, partieFlottante[:3]])
    return flottant


print(afficherFlottant(3.999999999))
