
tailleSimulation = 0
while(taille < 0 or taille > 100):
    try:
        tailleSimulation = int(input("Quelle est la taille de votre simulation?")
        assert tailleSimulation>0 and tailleSimulation<100
    except ValueError:
        print("Vous devez rentrer un nombre")
    except AssertionError:
        print("Vous devez rentrer un nombre supérieur à 0 et inférieur à 100")

for (x=0; x<tailleSimulation; x++):
                    
