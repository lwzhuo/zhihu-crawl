class status(object):
    def __init__(self):
        self.detList = {}

    def addStatus(self,step,detail):
        self.detList[step] = detail

    def showDetailList(self):
        str = ""
        dlist = self.detList.iterkeys()
        for item in dlist:
            str = str + (item+": "+self.detList.get(item)+"  ")
        return str