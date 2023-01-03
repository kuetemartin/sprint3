class Operation:
    def __init__(self, operation, resultat, date):
        self.operation = operation
        self.resultat = resultat
        self.date = date

    def getOperation (self):
        return self.operation

    def getResultat (self):
        return self.resultat

    def getDate(self):
        return self.date

    def setOperation(self, operation):
        self.operation = operation

    def setResultat(self, resultat):
        self.resultat = resultat

    def setDate(self, date):
        self.date = date




