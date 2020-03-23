from domain.Graph import Graph
import networkx as netx
class Repository:
    def __init__(self,filename):
        self.__filename=filename
        self.__graph=Graph(self.__readData())

    def __readData(self):
        graph=netx.read_gml("data\\input.gml")
        return graph

    def writeData(self,lines):
        f=open("output.txt","w")
        f.write('\n')
        for line in lines:
            f.write(line+'\n')
    def getGraph(self):
        return self.__graph
