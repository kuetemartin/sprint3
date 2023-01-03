class Ecran:
    def __init__(self, operation, resultat):
        self.operation = operation
        self.resultat = resultat

    def getOperation(self):
        return self.operation

    def resultat(self):
        return self.resultat

    def setOperation(self, operation):
        self.operation = operation

    def setResultat (self, resultat):
        self.reslutat = resultat