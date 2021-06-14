import math

class NBIris:
    def __init__(self, training, test):
        self.training = training
        self.test = test
        self.pFlower = {}   # P(flor)
        self.pAttr = {}     # P(atributo|flor)
        self.interval_attr = []  #intervalo de atributos

    # Discretiz dados de subdata
    def discret(self, subdata):

        # Calcula a qual classe o valor pertence
        f = lambda val, ini, step: math.floor((val - ini)/step)

        for data in subdata:
            for i_attr in range(4):

                if float(data[i_attr + 1]) < self.interval_attr[i_attr][0]:
                    data[i_attr + 1] = 0

                elif float(data[i_attr + 1]) >= self.interval_attr[i_attr][1]:
                    data[i_attr + 1] = int(f(self.interval_attr[i_attr][1], self.interval_attr[i_attr][0], self.interval_attr[i_attr][2]))

                else:
                    data[i_attr + 1] = int(f(float(data[i_attr + 1]), self.interval_attr[i_attr][0], self.interval_attr[i_attr][2]))


    # Calcula intervalo de classe
    def calculateInterval(self):
        # Tamanho do intervalo discreto para cada atributo
        step = []

        # Calcula limite superior do intevalo
        f = lambda finterval, fdf, flim_inf: finterval * fdf + flim_inf
        n_class = math.floor(math.sqrt(len(self.training))) # Aproximacao da regra de sturges

        # Cada atributo
        for i in range(1, 5):
            lim_inf = float(min(self.training, key=lambda a: a[i])[i])
            lim_sup = round(float(max(self.training, key=lambda a: a[i])[i]))

            step = (lim_sup - lim_inf) / n_class
            self.interval_attr.append([lim_inf, lim_sup, step])

    # Aprendendo as probabilidades
    def train(self):
        flowers = []
        universe = [[],[],[],[]]    # Contem todas as possibilidades de atributos

        for line in self.training:

            # Calcula qtd total de cada flor
            self.pFlower.setdefault(line[5], float(0))      # Verificacao de existencia de chave
            self.pFlower[line[5]] += 1
            flowers.append(line[5])

            # Calcula todas as possibilidades
            for i in range(4):
                var_step = 0
                mini = self.interval_attr[i][0]
                maxi = self.interval_attr[i][1]
                step = self.interval_attr[i][2]
                while (var_step * step) + mini <= maxi:
                    universe[i].append(var_step)
                    var_step += 1

        # Cria todas as possiveis chaves
        for f in flowers:
            for i in range(4):
                for u in universe[i]:
                    self.pAttr.setdefault(f, {})  # Verifica existencia de chave flor
                    self.pAttr[f].setdefault(i, {})  # Verifica existencia de chave attr
                    self.pAttr[f][i].setdefault(u, float(0))  # Verifica existencia de chave valor

        for line in self.training:

            # Calcula qtd total de cada par (flor, attr)
            for i in range(1,5):
                if line[5] not in self.pAttr:
                    print("A5 {} ID {}".format(line[5], line[0]))
                    print(self.interval_attr)
                if i-1 not in self.pAttr[line[5]]:
                    print("i-1 {} ID {}".format(i-1, line[0]))
                    print(self.interval_attr)
                if line[i] not in self.pAttr[line[5]][i-1]:
                    print("line(i) {} ID {}".format(line[i], line[0]))
                    print(self.interval_attr)
                self.pAttr[line[5]][i-1][int(line[i])] += 1

        # Freq relativa de (flor|attr)
        for k_flow, v_flow in self.pAttr.items():
            for k_attr, v_attr in v_flow.items():
                for k_val, v_val in v_attr.items():
                    self.pAttr[k_flow][k_attr][k_val] = (v_val + 1) / (self.pFlower[k_flow] + 1) # Bayes com bias

        # Freq relativa de flores
        for k, v in self.pFlower.items():
            self.pFlower[k] = v/len(self.training)  # Bayes com bias

        # print(self.pFlower)
        # print(self.pAttr)

    def predict(self):
        predict_list = []
        prob = []
        f = lambda fpf, fpa1, fpa2, fpa3, fpa4: fpf*fpa1*fpa2*fpa3*fpa4

        for t in self.test:

            a1 = t[1]
            a2 = t[2]
            a3 = t[3]
            a4 = t[4]

            for k_flower, v_flower in self.pFlower.items():
                name = k_flower

                pa1 = self.pAttr[name][0][a1]
                pa2 = self.pAttr[name][1][a2]
                pa3 = self.pAttr[name][2][a3]
                pa4 = self.pAttr[name][3][a4]
                prob.append([name, f(v_flower, pa1, pa2, pa3, pa4)])

            #     print("name {} pa1 {} pa2 {} pa3 {} pa4 {}".format(name, pa1, pa2, pa3, pa4))
            # print("########## Flower ###################")

            predict = max(prob, key=lambda a: a[1])[0]
            predict_list.append([t[0], predict])

        return predict_list
