class Xmldata:
    def __init__(self,val1,val = 'nil'):
        self.name = val1
        # name of this instances
        self.data = val
        # data stored in this instance
        self.elements = []
        # list that stores elements (instances of Xmldata)

    def addele(self,e):
        #adding an element
        self.elements.append(e)

    def delele(self,elename):
        #deleting an element by name
        for e in self.elements:
            if e.name == elename:
                self.elements.remove(e)
                print 'element removed\n'
                break

    def returnele(self,elename):
        # return particular element instance by getting name as input
        for e in self.elements:
            if e.name == elename:
                return e
        print 'element not found\n'
        return -1

    def isdata(self):
        # whether data is present
        return self.data!='nil'

    def have_elements(self):
        # whether it has elements
        return self.elements.count()!=0
