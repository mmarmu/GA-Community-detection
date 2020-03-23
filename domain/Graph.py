import networkx as netx
import scipy
class Graph:

    def __init__(self,graph):
        self.__graph=netx.convert_node_labels_to_integers(graph)
        self.__data = netx.to_dict_of_lists(self.__graph)
        self.__numpyGraph=netx.to_numpy_matrix(self.__graph)
    def existEdge(self,n1,n2):
        if n1>n2:
            n1,n2=n2,n1
        if(n1,n2) in self.__graph.edges:
            return True
        return False

    def getDegree(self,node):
        return len(self.__data[node])

    def getEdges(self):
        return self.__graph.edges

    def getNoNodes(self):
        return len(self.__data)

    def getNodes(self):
        return len(self.__data.keys())

    def getGraph(self):
        return self.__data

    def getStrangeGraph(self):
        return self.__graph

    def getMatrix(self):
        pass

    def getEdgeData(self,i,j):
        return self.__numpyGraph.item((i,j))

