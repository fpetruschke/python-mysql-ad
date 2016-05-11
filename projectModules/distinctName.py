class DistinctName:
    def __init__(self,struct):
        self.dnstruct = {}
        counter = len(struct) - 1
        while(counter >= 0):
            self.dnstruct[counter] = struct[counter]
            counter -= 1

    def makeDN(self,num = 0):
        dn = ''
        counter = num
        while (counter <= len(self.dnstruct)-1):
            if(counter != num):
                dn += ','
            if(counter +2 >= len(self.dnstruct)):
                dn += ' dc='
            elif(self.dnstruct[counter] == 'Users'):
                dn += ' cn='
            else:
                dn += ' ou='
            dn =  dn + self.dnstruct[counter]
            counter += 1
        return dn

    def addou(self,name):
        counter = len(self.dnstruct)
        tmp= []
        while(counter > 0):
            tmp[counter] = self.dnstruct[counter-1]
            counter -= 1
        tmp[0] = name
        return tmp
