class Xmldata:
    def __init__(self,val1,val = 'nil'):
        self.name = val1
        # name of this instances
        self.data = val
        # data stored in this instance
        self.elements = []
        # list that stores elements (instances of Xmldata)
        self.atts = []
        # list that stores mappings of attributes and their respective keys

    def addatt(self,attname,attval):
        # input - attribute name and value, then add it to the atts list
        self.atts.append((attname,attval))

    def delatt(self, attname):
        # deletes an attribute taking name as input
        for i in self.atts:
            if attname == i[0]:
                self.atts.remove(i)
                break

    def modifyatt(self,attname,attvalue):
        # modifies the value for the given attribute name, if not found adds it
        for i in self.atts:
            if attname == i[0]:
                self.atts.remove(i)
                break
        self.atts.append((attname,attvalue))

    def getattval(self,attname):
        # get attribute name
        for i in self.atts:
            if attname == i[0]:
                return i[1]
        print 'attribute not found'
        return -1

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

    def have_attributes(self):
        # whether it has attributes
        return self.atts.count()!=0
