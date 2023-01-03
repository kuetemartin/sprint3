
from ..models.boutons import Bouton


def ajoutBouton(text:str, bouton:Bouton):
    text.append(bouton.getValeur())
    return text

def evalExpression(expression:str):
    try:
        resultat = eval(expression)
        return resultat
    except:
        return " Errorr  .....! "