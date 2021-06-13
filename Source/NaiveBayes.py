
class NBIris:
    def __init__(self, training, test):
        self.training = training
        self.test = test
        self.pFlower = {}   # P(flor)
        self.pAttr = {}     # P(atributo|flor)

    # Aprendendo as probabilidades
    def train(self):

        for line in self.training:

            # Calcula qtd total de cada flor
            self.pFlower.setdefault(line[5], float(0))      # Verificacao de existencia de chave
            self.pFlower[line[5]] += 1

            # Calcula qtd total de cada par (flor, attr)
            for i in range(1,5):
                self.pAttr.setdefault(line[5], {})                      # Verifica existencia de chave flor
                self.pAttr[line[5]].setdefault(i, {})                   # Verifica existencia de chave attr
                self.pAttr[line[5]][i].setdefault(line[i], float(0))    # Verifica existencia de chave valor
                self.pAttr[line[5]][i][line[i]] += 1

        # Freq relativa de (flor|attr)
        for k_flow, v_flow in self.pAttr.items():
            for k_attr, v_attr in v_flow.items():
                for k_val, v_val in v_attr.items():
                    self.pAttr[k_flow][k_attr][k_val] = v_val / self.pFlower[k_flow]

        # Freq relativa de flores
        for k, v in self.pFlower.items():
            self.pFlower[k] = v/len(self.training)

        print(self.pFlower)
        print(self.pAttr)
