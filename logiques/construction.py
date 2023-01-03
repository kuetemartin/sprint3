from models.boutons import Bouton
from models.table  import Table
from models.calculatrice import Calculatrice
from models.Ecran import Ecran



def creationListeBoutons(listeElements:list):
    boutons = list()
    for element in listeElements:
        btn = Bouton(element, element, element)
        boutons.append(btn)
    return boutons

def creationTable(listeBoutons:list, label:str):
    table = Table(label,listeBoutons)
    return table

def creationCalculatrice(listeTable: list):
    ecran = Ecran('', 0)
    calculatrice = Calculatrice(ecran, listeTable)
    return calculatrice
