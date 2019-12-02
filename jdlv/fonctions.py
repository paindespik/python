from random import *


def DefinirTaille():
    tailleSimulation = 0
    while(tailleSimulation <= 0 or tailleSimulation > 100):
        try:
            tailleSimulation = int(input("Quelle est la taille de votre simulation? : "))
            assert tailleSimulation > 0 and tailleSimulation < 100
        except ValueError:
            print("Vous devez rentrer un nombre")
        except AssertionError:
            print("vous devez rentrer un nombre entre 0 et 100 non compris")
    return tailleSimulation


def InitialiserTableau(tailleSimulation, chanceApparition):
    simulation = []
    for i in range(0, tailleSimulation):
        line = []
        for j in range(0, tailleSimulation):
            if randint(0, tailleSimulation) < chanceApparition*tailleSimulation/100:
                line.append(True)
            else:
                line.append(False)
        simulation.append(line)
    return simulation


def AfficherTableau(simulation):
    for i in range(0, len(simulation)):
        for j in range(0, len(simulation)):
            if(simulation[i][j]):
                print("|#|", end='')
            else:
                print("| |", end='')
        print()


def PasserTour(simulation):
    listeDeTransition=InitialiserTableau(len(simulation), 0)
    for i in range(0, len(simulation)):
        for j in range(0, len(simulation)):
            entourage = 0
            if(i!=0):
                if simulation[i-1][j]:
                    entourage += 1
            
            if simulation[i-1][j-1]:
                entourage += 1
            if simulation[i][j-1]:
                entourage += 1
            if simulation[i+1][j-1]:
                entourage += 1
            if simulation[i+1][j]:
                entourage += 1
            if simulation[i+1][j+1]:
                entourage += 1
            if simulation[i][j+1]:
                entourage += 1
            if simulation[i-1][j-1]:
                entourage += 1
            if simulation[i][j]
