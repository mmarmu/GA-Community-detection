import networkx as netx
from random import randint


class Chromosome:
    def __init__(self, nr,genNumber,communities=None,):
        self.__genNumber=genNumber
        self.__fitness = 0
        self.__commNumber = nr
        if communities==None:
            self.__communities=[]
        else:
            self.__communities = communities
        self.__initial()


    def __initial(self):
        self.__communities = [0] * self.__commNumber
        currentNrOfComm = 1
        self.__communities[0] = 1
        for i in range(self.__commNumber):
            randomCommNumber = randint(1, currentNrOfComm + 1)
            self.__communities[i] = randomCommNumber
            if randomCommNumber > currentNrOfComm:
                currentNrOfComm += 1

        self.__commNumber = currentNrOfComm

    def mutation(self):
        randPosition = randint(0, len(self.__communities) - 1)
        self.__communities[randPosition] = randint(0, len(self.__communities) - 1)
        self.linearizeCommunities()

    def linearizeCommunities(self):
        nr=len(self.__communities)
        currentCom=1
        appear=False
        for i in range(nr):
            if self.__communities[i]<currentCom:
                continue
            if self.__communities[i]==currentCom:
                appear=True
                continue
            if appear:
                currentCom+=1
                if self.__communities[i]==currentCom:
                    continue
                appear=False

            if self.__communities[i]>currentCom:
                self.__prettySwap(self.__communities[i],currentCom)
                appear=True

        self.__commNumber=currentCom
        # newCom = [0] * self.__commNumber
        # nr = 0
        # for el in self.__communities:
        #     if newCom[el-1] == 0:
        #         nr += 1
        #         newCom[el-1] = 1
        #
        # self.__commNumber = nr
        # for i in range(1, self.__commNumber + 1):
        #     maxCom = self.findMaxCommunity()
        #     for j in range(self.__commNumber):
        #         if self.__communities[j] == maxCom:
        #             self.__communities[j] = i

    def findMaxCommunity(self):
        return max(self.__communities)

    def crossover(self, other):
        newCommunity = [0] * len(self.__communities)
        pivot=randint(0,(len(self.__communities)/2))
        for i in range(pivot):
            newCommunity[i]=self.__communities[i]
        for i in range(pivot,len(self.__communities)):
            newCommunity[i]=other.getCommunities()[i]

        newChromo=Chromosome(nr=len(newCommunity),communities=newCommunity,genNumber=self.getGenNumber())
        newChromo.linearizeCommunities()
        return newChromo

    def getCommunities(self):
        return self.__communities

    def getCommNumber(self):
        return self.__commNumber

    def getFitness(self):
        return self.__fitness

    def setFitness(self, val):
        self.__fitness = val

    def __str__(self):
        return '\nChromo: ' + str(self.__communities) + ' has fit: ' + str(self.__fitness)

    def __prettySwap(self,first ,second):
        for i in range(len(self.__communities)):
            if self.__communities[i]==first:
                self.__communities[i]=-1

        for i in range(len(self.__communities)):
            if self.__communities[i]==second:
                self.__communities[i]=first

        for i in range(len(self.__communities)):
            if self.__communities[i]==-1:
                self.__communities[i]=first


    def getGenNumber(self):
        return self.__genNumber

    def setGenNumber(self,gen):
        self.__genNumber=gen
#
# def __repr__(self):
#     return self.__str__()
#
# def __eq__(self, c):
#     return self.__repres == c.__repres and self.__fitness == c.__fitness
