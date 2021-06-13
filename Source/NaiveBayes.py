
class NBIris:
    def __init__(self, training, test):
        self.training = training
        self.test = test
        self.pFlower = {}   # P(flor)
        self.pAttr = {}     # P(atributo|flor)

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
            for i in range(1,5):
                if line[i] not in universe[i-1]:
                    universe[i-1].append(line[i])

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
                self.pAttr[line[5]][i-1][line[i]] += 1

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
                #print("name {} a1 {} a2 {} a3 {} a4 {}".format(name, a1, a2, a3, a4))
                pa1 = self.pAttr[name][0][a1]
                pa2 = self.pAttr[name][1][a2]
                pa3 = self.pAttr[name][2][a3]
                pa4 = self.pAttr[name][3][a4]
                prob.append([name, f(v_flower, pa1, pa2, pa3, pa4)])
                print(v_flower)
            predict = max(prob, key=lambda a:a[1])[0]
            predict_list.append([t[0], predict])

        return predict_list
