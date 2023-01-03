class Table:

    def __init__ (self,label, listeBoutons):
        self.label = label
        self.listeBoutons = listeBoutons

    def getLabel(self):
        return self.label

    def getlisteBoutons(self):
        return self.listeBoutons

    def getmax_nbr(self):
        return self.max_nbr

    def setLabel(self, label):
        self.label = label

    def setlisteBoutons(self, listeBoutons):
        self.listeBoutons = listeBoutons

    def setMax_nbr(self, max_nbr):
        self.max_nbr = max_nbr