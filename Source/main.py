# Israel Rocha #
# Algorithm knn. Iris Dataset #


from Source.data_handle import DataHandle
from Source.KNN import IrisKNN

# Pega caminho de dados
def getPath():
    # folder = ""   # Use as auto path if want
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
    return path

if __name__ == '__main__':

    # le CSV #
    subset = DataHandle(getPath())
    subset.readCSV()

    # Knn
    subset.trainingSet(0.7) # 70%
    knn = IrisKNN(subset.training, subset.test)
    predict = knn.kNearest(5)
    acc = subset.accuracy(predict)

    # Results #

    # Shows truth X predict
    subset.showsDiff(predict)

    # Accuracy
    print(acc)