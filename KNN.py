import math

class IrisKNN:

    def __init__(self, training, test):

        # funcao de distancia
        self.fd = lambda x1, x2, x3, x4, _x1, _x2, _x3, _x4: math.sqrt(
            (x1 - _x1) ** 2 + (x2 - _x2) ** 2 + (x3 - _x3) ** 2 + (x4 - _x4) ** 2)
        self.training = training
        self.test = test

    # Calcula as distancias e verifica os k-proximos
    def kNearest(self, k):
        predict_list = []

        # Verificando tamanho de K
        if k > len(self.training):
            print("K is bigger than training set. Closign application...\n")
            return 0

        # Teste
        for t in self.test:
            distant = []
            flower = {}

            # print("########################")
            distance = self.euclidianDistance(t)

            # Ordena de acordo com proximidade
            distance = sorted(distance, key=lambda dx: dx[2])

            #for line in distant:
            #   print(line)

            flower = IrisKNN.classification(k, distance)
            predict_list.append([t[0], list(flower.keys())[0]])  # Extract ID and name predicted
        return predict_list

    # t -> to predict.
    def euclidianDistance(self, t):
        distant = []
        for x in self.training:
            # Distant contem (ID, nome da flor, distancia com relacao a t)
            distant.append([x[0], x[5],
                            self.fd(float(x[1]), float(x[2]), float(x[3]), float(x[4]), float(t[1]), float(t[2]),
                                    float(t[3]), float(t[4]))])
        return distant

    # Classifica com base nos K-proximos e lista de distancia
    def classification(k, distance):
        flowers = {}
        total = 0

        # Soma dos K's mais proximos
        for i in range(k):
            flowers.setdefault(distance[i][1], int(0))
            flowers[str(distance[i][1])] += 1

        # Classifica quem teve mais ocorrência
        for flow_name, value in flowers.items():
            if value > total:
                name = flow_name
                total = value
        return {name: total}
