from ga.GA import GA
import numpy as np
import networkx as netx
import matplotlib.pyplot as plt

class Service:
    def __init__(self,repo):
        self.__repo=repo

    def generate(self,generationsNumber,populationSize):
        ga=GA(self.__repo.getGraph(),populationSize)
        output=[]
        for i in range(1,generationsNumber+1):
            ga.oneGenerationElitism()
            outt="\nGENERATION: "+str(i)+"| FITNESS: " + str(ga.getBestFitness())+"| NR: "+ str(ga.getBestCommunitiesNumber())
            output+=[outt]

        comm=ga.getBestCommunities()

        output+=["BEST COMMUNITY \n|NOD - COMUNITATE|"]
        for i in range(len(comm)):
            output+=[str(i)+" - "+str(comm[i])]



        self.__repo.writeData(output)
        G = self.__repo.getGraph().getStrangeGraph()
        pos = netx.spring_layout(G)  # compute graph layout
        plt.figure(figsize=(4, 4))  # image is 8 x 8 inches
        netx.draw_networkx_nodes(G, pos, node_size=600, node_color=comm)
        netx.draw_networkx_edges(G, pos, alpha=0.3)
        plt.show(G)
        return output