from fonctions import *

tailleSimulation = DefinirTaille()


simulation = InitialiserTableau(tailleSimulation, 10)
while(True):
    AfficherTableau(simulation)
    input('Hit <Return> to continue')
    simulation = PasserTour(simulation)
