from logiques.construction import creationListeBoutons, creationTable, creationCalculatrice
from models.boutons import Bouton

def test():
    tab = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '/', '*']
    #boutons:list(Bouton) = creationListeBoutons(tab)
    boutons = creationListeBoutons(tab)
    table = creationTable(boutons, 'nombre')
    calculatrice = creationCalculatrice([table])

    print(calculatrice.getlisteTable()[0].getlisteBoutons()[10].getLabel())

