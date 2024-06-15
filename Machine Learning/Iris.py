from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def CheckIris(Features,Label,sepalWidth,sepalLength,petalWidth,petalLenght):

    obj = tree.DecisionTreeClassifier()

    obj.fit(Features,Label)

    ret = obj.predict([[]])

def main():

    iris = load_iris()

    Features = iris.data
    Labels = iris.target

    print(Features)
    print(Labels)

    data_train,data_test,target_train,target_test = train_test_split(Features,Labels,test_size = 0.5)


if __name__ == "__main__":
    main()