class Bouton:

    def __init__ (self,label, type, valeur):
        self.label = label
        self.type = type
        self.valeur = valeur

    def getLabel (self):
        return self.label

    def getType (self):
        return self.type

    def getValeur(self):
        return self.valeur

    def setLabel (self, label):
        self.label = label

    def setType(self, type):
        self.type = type

    def setValeur(self, valeur):
        self.valeur = valeur