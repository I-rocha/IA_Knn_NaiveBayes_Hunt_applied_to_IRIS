# Israel Rocha #
# Algorithm knn. Iris Dataset #

import csv
import math


def printContent(data):
    for row in data:
        for single in row:
            print(single)


class IrisKNN:

    def __init__(self, path):
        self.path = path  # path do csv
        self.data = []  # inicia com dados vazios
        self.training = []  #
        self.test = []  # Dados para teste

        # funcao de distancia
        self.fd = lambda x1, x2, x3, x4, _x1, _x2, _x3, _x4: math.sqrt(
            (x1 - _x1) ** 2 + (x2 - _x2) ** 2 + (x3 - _x3) ** 2 + (x4 - _x4) ** 2)

    # Le arquivo csv separado por ','
    def readCSV(self):

        # abre arquivo
        with open(self.path, mode='r') as file:
            # objeto
            reader = csv.reader(file)

            # Cada linha
            for row in reader:
                self.data.append(row)

            # Elimina primeira linha
            self.data.pop(0)

    # Imprime elementos um a um
    def trainingSet(self, percent):
        tr_size = math.floor(len(self.data) * percent)
        self.training = self.data[:tr_size]
        self.test = self.data[tr_size:]

    # Calcula as distancias e verifica os k-proximos
    def kNearest(self, k):
        # distant = []

        # Verificando tamanho de K
        if k > len(self.training):
            print("K is bigger than training set. Closign application...\n")
            return 0

        for t in self.test:
            distant = []
            flowers = {}
            maximum = 0

            # print("########################")

            for x in self.training:
                # Distant contem (ID, nome da flor, distancia com relacao a t)
                distant.append([x[0], x[5],
                                self.fd(float(x[1]), float(x[2]), float(x[3]), float(x[4]), float(t[1]), float(t[2]),
                                        float(t[3]), float(t[4]))])

            # Ordena de acordo com a distancia
            distant = sorted(distant, key=lambda dx: dx[2])

            for line in distant:
                print(line)

            # Seleciona os K's mais proximos
            for i in range(k):
                flowers.setdefault(distant[i][1], int(0))
                flowers[str(distant[i][1])] += 1

            # Soma dos K's mais proximos
            for flow_name, value in flowers.items():
                if value > maximum:
                    name = flow_name
                    maximum = value
            print("Name: {} ID:{} {}".format(name, t[0], value))

    # Lista todas as distancias
    # def listDistant(self):


if __name__ == '__main__':
    # folder = ""   # Use as automatically path if wants
    folder = ""
    filename = "Iris.csv"
    print("Starting application...\n")
    print("Select:\n(1)If csv is in the same folder as .py")
    print("(2)If want to put manually the entire path (Ex: C:/somefolder/Iris.csv)\n")

    opt = int(input())

    # path padrao
    if opt == 1:
        path = folder + filename
        print(folder + filename)

    # path manual
    elif opt == 2:
        path = str(input("input path...\n"))

    # erro
    else:
        print("Option invalid...closing application\n")

    knn = IrisKNN(folder + filename)
    knn.readCSV()
    knn.trainingSet(0.7)

    knn.kNearest(5)

    # knn.printContent(knn.test)
    # knn.printContent()