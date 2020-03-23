from service.Service import Service
class UI:
    def __init__(self,serv):
        self.__serv=serv

    def run(self):
        nrGen=int(input("Numarul de generatii:"))
        nrPop=int(input("Dimensiunea populatiei"))
        rez=self.__serv.generate(nrGen,nrPop)
        for el in rez:
            print(el)
