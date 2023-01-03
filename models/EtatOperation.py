class EtatOperation:
    def __init__(self, operation, etat):
        self.operation = operation
        self.etat = etat

    def getOperation (self):
        return self.operation

    def getEtat(self):
        return self.etat

    def setOperation(self, operation):
        self.operation = operation

    def setEtat(self, etat):
        self.etat = etat
