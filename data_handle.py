import csv
import math


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

    # Separa os elementos de treinamento e teste
    def trainingSet(self, percent):
        tr_size = math.floor(len(self.data) * percent)
        self.training = self.data[:tr_size]
        self.test = self.data[tr_size:]

    @ staticmethod
    # Imprime elementos um a um
    def printContent(data):
        for row in data:
            for single in row:
                print(single)