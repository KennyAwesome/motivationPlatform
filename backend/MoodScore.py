class Mood():
    def __init__(self):
        self.absolutValue = 0
        self.pointStarred = 20
        self.pointRegular = 10
        # These are constants
        self.pleasureBase = -0.88 # need to be experimented
        self.pleasureFactor = 0.2
        self.expressionRange = 5 # range is how many expression is possible

    def lookupPleasure(self):
        #pleasure = self.pleasureBase**(self.pleasureFactor*self.absolutValue)+1
        pleasure = -0.88**(0.2*self.absolutValue) + 1
        #print(pleasure)
        for pleasureCategory in range(1,self.expressionRange+1):
            actualCounter = (self.expressionRange - pleasureCategory)
            schritt = 100/self.expressionRange
            schranke = float(actualCounter*schritt)/100
            #print(schranke)
            if(schranke < pleasure):
                return actualCounter

    def updateAbsoluteValue(self, isDone, isStarred):
        print("yasy")
        if isDone:
            if isStarred:
                self.absolutValue += self.pointStarred
            else:
                self.absolutValue += self.pointRegular
                #print(self.pointRegular)
        else:
            if isStarred:
                if(self.absolutValue > self.pointStarred):
                    self.absolutValue -= self.pointStarred
            else:
                if (self.absolutValue > self.pointRegular):
                    self.absolutValue -= self.pointRegular


    def updateLoookupParameter(self):
        return 0
        # max number of possible -> normalize targetValue/maxValue


# usage
#m = Mood()
#m.absoluteValue = 42 # you can set it the hard way
#m.updateAbsoluteValue(isDone=False,isStarred=False)
#pleasureCategory = m.lookupPleasure() #range is (1 - 4)