from ga.Chromosome import Chromosome
from random import randint
class GA:
    def __init__(self,graph,popSize):
        self.__graph=graph
        self.__population=[]
        self.__bestChromo=None
        self.__init(popSize)
        self.__currentGen=1


    def __init(self,populationSize):
        for i in range(populationSize):
            self.__population.append(Chromosome(nr=self.__graph.getNoNodes(),genNumber=1))

    def evaluation(self):
        bestFit=-99999999
        for chromo in self.__population:
            fit=self.modularity(chromo.getCommunities())
            chromo.setFitness(fit)
            if fit>bestFit:
                bestFit=fit
                self.__bestChromo=chromo
                self.__bestChromo.setGenNumber(self.__currentGen)


    def modularity(self,communities):
        noNodes = self.__graph.getNoNodes()
        mat = self.__graph.getMatrix()
        noEdges = len(self.__graph.getEdges())
        M = 2 * noEdges
        Q = 0.0
        for i in range(0, noNodes):
            for j in range(0, noNodes):
                if (communities[i] == communities[j]):
                    Q += (self.__graph.getEdgeData(i,j) - self.__graph.getDegree(i) * self.__graph.getDegree(j) / M)
        return Q * 1 / M


    def selection(self):
        pos1 = randint(0,len(self.__population)-1)
        pos2 = randint(0,len(self.__population)-1)

        if self.__population[pos1].getFitness()>self.__population[pos2].getFitness():
            return pos1
        return pos2

    def oneGeneration(self):
        newPopulation=[]
        for i in range(len(self.__population)):
            chromo1 = self.__population[self.selection()]
            chromo2 = self.__population[self.selection()]

            off=chromo1.crossover(chromo2)
            off.mutation()
            newPopulation.append(off)

        self.__population=newPopulation.copy()
        self.evaluation()

    def oneGenerationElitism(self):
        newPopulation=[]
        if self.__bestChromo!=None:
            newPopulation.append(self.__bestChromo)
        else:
            newPopulation.append(self.__population[self.selection()])

        for i in range(len(self.__population)-1):
            chromo1 = self.__population[self.selection()]
            chromo2 = self.__population[self.selection()]

            off=chromo1.crossover(chromo2)
            off.mutation()
            newPopulation.append(off)

        self.__population=newPopulation.copy()
        self.__currentGen+=1
        self.evaluation()


    def oneGenerationSteadyState(self):
        for i in range(len(self.__population)):
            chromo1 = self.__population[self.selection()]
            chromo2 = self.__population[self.selection()]

            off =chromo1.crossover(chromo2)
            off.mutation()
            off.setFitness(self.modularity(off.getCommunities()))
            worst=self.worstChromosomeIndex()

            if off.getFitness()>self.__population[worst].getFitness():
                self.__population[worst]=off

        self.updateBestChromo()
    def getBestFitness(self):
        return self.__bestChromo.getFitness()

    def getBestCommunitiesNumber(self):
        return self.__bestChromo.getCommNumber()

    def getBestCommunities(self):
        return self.__bestChromo.getCommunities()

    def getBestGeneration(self):
        return self.__bestChromo.getGenNumber()

    def worstChromosomeIndex(self):
        mini=min(self.__population,key=lambda x:x.getFitness())
        for i in range(len(self.__population)):
            if mini==self.__population[i]:
                return i

    def updateBestChromo(self):
        maxi=max(self.__population,key=lambda x:x.getFitness())
        self.__bestChromo=maxi
