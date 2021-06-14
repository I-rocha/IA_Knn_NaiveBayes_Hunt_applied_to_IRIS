import csv
import math
import random

class DataHandle:

    def __init__(self, path):
        print("Inside function")
        self.path = path  # path do csv
        self.data = []  # inicia com dados vazios
        self.training = []  # Dados de treinamento
        self.test = []  # Dados para teste

    # Le arquivo csv separado por ','
    def readCSV(self):
        print("Reading csv")
        # abre arquivo
        with open(self.path, mode='r') as file:
            # objeto
            reader = csv.reader(file)

            # Cada linha
            for row in reader:
                self.data.append(row)

            # Elimina primeira linha
            self.data.pop(0)

    # Separa os elementos de treinamento e teste aleatoriamente
    def trainingSet(self, percent):
        tr_size = math.floor(len(self.data) * percent)
        test_size = len(self.data) - tr_size
        temp_data = self.data.copy()
        random.shuffle(temp_data)
        self.training = temp_data[:tr_size]
        self.test = temp_data[tr_size:]

    # Imprime comparação entre real e predito
    def showsDiff(self, list_predict):
        print("")
        for i in range(len(list_predict)):
            ID = int(list_predict[i][0])
            index = ID - 1
            print(self.test[i][0])  # ID
            print("Truth: {}\nPredict: {}".format(self.data[index][5], list_predict[i][1]))
            print("")

    # Acuracia (acertos/total)
    def accuracy(self, list_predict):
        truth = 0
        error = 0
        for i in range(len(list_predict)):
            ID = int(list_predict[i][0])
            index = ID - 1
            if list_predict[i][1] == self.data[index][5]:
                truth += 1
            else:
                error += 1
        return truth/len(list_predict)


    @ staticmethod
    # Imprime elementos um a um
    def printContent(data):
        for row in data:
            for single in row:
                print(single)
